#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - c64 Python helper.

Some classes that represent c64 structures.
This file can also be imported as a module.
It contains the following classes:

- Window - a basic pygame window for displaying stuff
- Memory - a basic pygame window for displaying stuff
- Bitmap - A c64 bitmap representation
- Char - The representation of a single c64 character
- Screen - The representation of c64 screen
- Methods for writing binary contents
"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2016-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.20.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import pygame
from typing import List
from typing import Tuple



# --- class definitions -----------------------------------------------------

# --- Char class ------------------------------------------------------------
class Char:
    """A single c64 character"""

    def __init__(self, data : Tuple[int] = None):
        """Constructor, allocates memory.

        Assigns the given data. If no data is given, the data (character)
        is initialiased with zeros.

        Args:
            data (Tuple[int]): The character data (should be 8 bytes long)
        """
        self.data = data
        if self.data==None:
            self.data = [0]*8


    def draw_at(self, surface : pygame.Surface, x : int, y : int, fgColor : Tuple[int, int, int, int]=(255, 255, 255, 255), bgColor : Tuple[int, int, int, int]=(0, 0, 0, 255)):
        """Draws this character (in hires) at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            fgColor (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bgColor (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
        """
        for yl in range(0, 8):
            b = self.data[yl]
            for xl in range(0, 8):
                c = bgColor
                if b&(2**(7-xl))!=0:
                    c = fgColor
                if c:
                    surface.set_at((xl+x, yl+y), c)


    def draw_at_multicolor(self, surface : pygame.Surface, x : int, y : int, fgColor : Tuple[int, int, int, int]=(255, 255, 255, 255), bgColor : Tuple[int, int, int, int]=(0, 0, 0, 255), multi1Color : Tuple[int, int, int, int]=(192, 192, 192, 255), multi2Color: Tuple[int, int, int, int]=(128, 128, 128, 255)):
        """Draws this character in multicolor at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            fgColor (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bgColor (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
            multi1Color (Tuple[int, int, int, int]): multi1 color given as a tuple of four integers (rgba), may be None
            multi2Color (Tuple[int, int, int, int]): multi2 color given as a tuple of four integers (rgba), may be None
        """
        for yl in range(0, 8):
            b = self.data[yl]
            for xl in range(0, 4):
                c = bgColor
                if b&(2**(7-xl*2))!=0 and b&(2**(7-xl*2-1))!=0:
                    c = fgColor
                elif b&(2**(7-xl*2))!=0 and b&(2**(7-xl*2-1))==0:
                    c = multi1Color
                elif b&(2**(7-xl*2))==0 and b&(2**(7-xl*2-1))!=0:
                    c = multi2Color
                if c:
                    surface.set_at((xl*2+x, yl+y), c)
                    surface.set_at((xl*2+x+1, yl+y), c)


    def same(self, c) -> bool:
        """Returns whether the given character is same as this one.

        Args:
            c (Char): The character to compare this character to

        Returns:
            (bool): Whether the given character is same as self
        """
        for i,x in enumerate(self.data):
            if self.data[i]!=c.data[i]:
                return False
        return True


    def write(self, f):
        """Writes this character to a file.

        Args:
            f (file descriptor): The file to write this character to
        """
        f.write(bytearray(self.data))


    def inverse(self):
        """Inverses this character."""
        for i,b in enumerate(self.data):
            self.data[i] ^= 255
            
            
            
# --- Window class ----------------------------------------------------------
class Window(object):
    """A plain pygame window. Nothing special about it."""

    def __init__(self, w : int, h : int, title : str = "c64 draw"):
        """Generates and shows a pygame window.

        Args:
            w (int): window width
            h (int): window height
            title (str): the window title
        """
        import pygame
        import pygame.gfxdraw
        import pygame.locals
        pygame.init()
        self.show = True
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(title)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((200,200,10))
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()


    def run(self):
        """Processes the pygame window events.

        Should be called in a loop to process the occuring events.
        Sets the self.show flag to False when being closed.
        """
        import pygame
        import pygame.gfxdraw
        import pygame.locals
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.show = False
            if event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_ESCAPE:
                self.show = False




# --- Memory class ----------------------------------------------------------
class Memory:
    """The representation of a c64 memory."""

    def __init__(self, data : List[int] = None):
        """Constructor

        Assigns the given data. If no data is given, the data (memory)
        is initialiased with zeros.

        Args:
            data (List[int]): The memory data (should be 65536 bytes long)
        """
        self.data = data
        if self.data==None:
            self.data = [0]*(65536)


    def load(self, filename : str):
        """Loads the given files as a memory dump.

        Reads the first two bytes as destination (starting address).
        Reads the reminder starting at this address, the rest of the memory
        is filled with zeros.

        Loading assures that the memory is complete (is 65536 bytes long)

        Args:
            filename (str): The file to load

        TODO: check destination byte order (not spent a thought on it)
        """
        f = open(filename, "rb")
        ba = bytearray(f.read())
        startingAddress = ba[0] + ba[1] * 256
        self.data = []
        if startingAddress!=0:
            self.data = [0] * startingAddress
        self.data.extend(list(ba[2:]))
        rest = 65536 - (startingAddress + len(ba) - 2)
        if rest>0:
            self.data.extend([0]*rest)


    def draw_at(self, surface : pygame.Surface, x : int, y : int, cols : int, fgColor : Tuple[int, int, int, int]=(255, 255, 255, 255), bgColor : Tuple[int, int, int, int]=(0, 0, 0, 255)):
        """Draws this memory at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            cols (int): the number of (character) columns
            fgColor (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bgColor (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
        """
        hc = int(65536/8/cols) # rows in chars
        for yh in range(0, hc):
            for xh in range(0, cols):
                offset = xh*8 + yh*8*cols
                char = Char(self.data[offset:offset+8])
                char.draw_at(surface, x+xh*8, y+yh*8, fgColor, bgColor)


    def char_at(self, addr : int) -> Char:
        """Returns the eight bytes at the given address as a char

        Args:
            addr (int): The address to read the bytes from

        Returns:
            (Char): The character built from the bytes at the given address
        """
        return Char(self.data[addr:addr+8])




# --- Bitmap class ----------------------------------------------------------
class Bitmap:
    """The representation of a c64 bitmap."""

    def __init__(self, data : List[int] = None):
        """Constructor

        Assigns the given data. If no data is given, the data (bitmap)
        is initialiased with zeros.

        Args:
            data (List[int]): The bitmap data
        """
        self.data = data
        if self.data==None:
            self.data = [0]*(40*25*8)


    def char_at(self, col : int, row : int) -> Char:
        """Returns the Char representation of the character at the given position.

        Args:
            col (int): The column (in characters) to read the char from
            row (int): The row (in characters) to read the char from

        Returns:
            (Char): The character built from the bytes at the given column and row
        """
        off = row*40*8+col*8
        return Char(self.data[off:off+8])


    def draw_at(self, surface : pygame.Surface, x : int, y : int, fgColor : Tuple[int, int, int, int]=(255, 255, 255, 255), bgColor : Tuple[int, int, int, int]=(0, 0, 0, 255)):
        """Draws this bitmap at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            fgColor (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bgColor (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
        """
        for yh in range(0, 25):
            for xh in range(0, 40):
                for yl in range(0, 8):
                    b = self.data[yh*8*40+xh*8+yl]
                    for xl in range(0, 8):
                        c = bgColor
                        if b&(2**(7-xl))!=0:
                            c = fgColor
                        if c:
                            surface.set_at((xh*8+xl+x, yh*8+yl+y), c)


    def from_surface(self, surface : pygame.Surface, x : int, y : int):
        """Generates the Bitmap from the given surface, starting at the given position.

        Please note that only white pixels are assumed to be set

        Args:
            surface (pygame.Surface): The surface to extract the bitmap from
            x (int): x-offset for reading
            y (int): y-offset for reading
        """
        w = (255,255,255,255)
        for yh in range(0, 25):
            for xh in range(0, 40):
                for yl in range(0, 8):
                    v = 0
                    for xl in range(0, 8):
                        c = 0
                        v = v*2
                        if surface.get_at((xh*8+xl+x, yh*8+yl+y))==w:
                            c = 1
                        v = v+c
                    self.data[yh*8*40+xh*8+yl] = v


    def from_c64_screen(self, screen, chars : List[Char]):
        """Fills the bitmap using the given screen and character set information

        Args:
            screen (Bitmap): The screen to use
            chars (List[Char]): The character set to use
        """
        for yh in range(0, 25):
            for xh in range(0, 40):
                char = screen.char_at(xh, yh)
                for yl in range(0, 8):
                    v = 0
                    for xl in range(0, 8):
                        c = 0
                        v = v*2
                        if chars[char].data[yl]&(2**(7-xl)):
                            c = 1
                        v = v+c
                    self.data[yh*8*40+xh*8+yl] = v



# --- Screen class ----------------------------------------------------------
class Screen:
    """The representation of a c64 screen"""

    def __init__(self, data : List[int]=None):
        """Constructor, allocates memory.

        Assigns the given data. If no data is given, the data (screen)
        is initialiased with zeros.

        Args:
            data (List[int]): The screen data (should be 1000 bytes long)
        """
        self.data = data
        if self.data==None:
            self.data = [0]*(40*25)


    def char_at(self, col : int, row : int) -> int:
        """Returns the caracter at the given position

        Args:
            col (int): The column to get the character from
            row (int): The row to get the character from

        Returns:
            (int): The character at the given row and column
        """
        return self.data[col+row*40]


    def set_char_at(self, col : int, row : int, char : int):
        """Sets the given character at the given position

        Args:
            col (int): The column to set the character at
            row (int): The row to set the character at
            char (int): The character to set
        """
        self.data[col+row*40] = char

