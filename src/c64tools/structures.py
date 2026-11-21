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
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
from typing import List, Tuple
import os
import sys
import pygame



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
        if self.data is None:
            self.data = [0]*8


    def draw_at(self, surface : pygame.Surface, x : int, y : int, fg_color : Tuple[int, int, int, int]=(255, 255, 255, 255), bg_color : Tuple[int, int, int, int]=(0, 0, 0, 255)) -> None:
        """Draws this character (in hires) at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            fg_color (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bg_color (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
        """
        for yl in range(0, 8):
            b = self.data[yl]
            for xl in range(0, 8):
                c = bg_color
                if b&(2**(7-xl))!=0:
                    c = fg_color
                if c:
                    surface.set_at((xl+x, yl+y), c)


    def draw_at_multicolor(self, surface : pygame.Surface, x : int, y : int, fg_color : Tuple[int, int, int, int]=(255, 255, 255, 255), bg_color : Tuple[int, int, int, int]=(0, 0, 0, 255), multi_color1 : Tuple[int, int, int, int]=(192, 192, 192, 255), multi_color2: Tuple[int, int, int, int]=(128, 128, 128, 255)) -> None:
        """Draws this character in multicolor at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            fg_color (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bg_color (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
            multi_color1 (Tuple[int, int, int, int]): multi1 color given as a tuple of four integers (rgba), may be None
            multi_color2 (Tuple[int, int, int, int]): multi2 color given as a tuple of four integers (rgba), may be None
        """
        for yl in range(0, 8):
            b = self.data[yl]
            for xl in range(0, 4):
                c = bg_color
                if b&(2**(7-xl*2))!=0 and b&(2**(7-xl*2-1))!=0:
                    c = fg_color
                elif b&(2**(7-xl*2))!=0 and b&(2**(7-xl*2-1))==0:
                    c = multi_color1
                elif b&(2**(7-xl*2))==0 and b&(2**(7-xl*2-1))!=0:
                    c = multi_color2
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
        for i,_ in enumerate(self.data):
            if self.data[i]!=c.data[i]:
                return False
        return True


    def write(self, f) -> None:
        """Writes this character to a file.

        Args:
            f (file descriptor): The file to write this character to
        """
        f.write(bytearray(self.data))


    def inverse(self) -> None:
        """Inverses this character."""
        for i,_ in enumerate(self.data):
            self.data[i] ^= 255
            
            
            
# --- Window class ----------------------------------------------------------
class Window:
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


    def run(self) -> None:
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


    def load(self, filename : str) -> None:
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
        starting_address = ba[0] + ba[1] * 256
        self.data = []
        if starting_address!=0:
            self.data = [0] * starting_address
        self.data.extend(list(ba[2:]))
        rest = 65536 - (starting_address + len(ba) - 2)
        if rest>0:
            self.data.extend([0]*rest)


    def draw_at(self, surface : pygame.Surface, x : int, y : int, cols : int, fg_color : Tuple[int, int, int, int]=(255, 255, 255, 255), bg_color : Tuple[int, int, int, int]=(0, 0, 0, 255)) -> None:
        """Draws this memory at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            cols (int): the number of (character) columns
            fg_color (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bg_color (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
        """
        hc = int(65536/8/cols) # rows in chars
        for yh in range(0, hc):
            for xh in range(0, cols):
                offset = xh*8 + yh*8*cols
                char = Char(self.data[offset:offset+8])
                char.draw_at(surface, x+xh*8, y+yh*8, fg_color, bg_color)


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
        if self.data is None:
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


    def draw_at(self, surface : pygame.Surface, x : int, y : int, fg_color : Tuple[int, int, int, int]=(255, 255, 255, 255), bg_color : Tuple[int, int, int, int]=(0, 0, 0, 255)) -> None:
        """Draws this bitmap at the given surface and the given position.

        Args:
            surface (pygame.Surface): The surface to draw this memory to
            x (int): x-offset for drawing
            y (int): y-offset for drawing
            fg_color (Tuple[int, int, int, int]): foreground color given as a tuple of four integers (rgba), may be None
            bg_color (Tuple[int, int, int, int]): background color given as a tuple of four integers (rgba), may be None
        """
        for yh in range(0, 25):
            for xh in range(0, 40):
                for yl in range(0, 8):
                    b = self.data[yh*8*40+xh*8+yl]
                    for xl in range(0, 8):
                        c = bg_color
                        if b&(2**(7-xl))!=0:
                            c = fg_color
                        if c:
                            surface.set_at((xh*8+xl+x, yh*8+yl+y), c)


    def from_surface(self, surface : pygame.Surface, x : int, y : int) -> None:
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


    def from_c64_screen(self, screen, chars : List[Char]) -> None:
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
        if self.data is None:
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


    def set_char_at(self, col : int, row : int, char : int) -> None:
        """Sets the given character at the given position

        Args:
            col (int): The column to set the character at
            row (int): The row to set the character at
            char (int): The character to set
        """
        self.data[col+row*40] = char

