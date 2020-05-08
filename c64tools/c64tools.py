"""c64

Some classes that represent c64 structures.

This file can also be imported as a module and contains the following
classes:

    * Window - a basic pygame window for displaying stuff
    * Memory - a basic pygame window for displaying stuff
    * Bitmap - A c64 bitmap representation
    * Char - The representation of a single c64 character
    * Screen - The representation of c64 screen
    * Methods for writing binary contents

TODO: remove dependency on pygame
TODO: refactor binary writer helper methods
TODO: add a Sprite class

(c) Daniel Krajzewicz 2016-2020
daniel@krajzewicz.de

Available under GPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import pygame
import pygame.gfxdraw
import pygame.locals


# --- Window class --------------------------------------------------
class Window(object):
  """A plain pygame window. Nothing special about it."""
  
  def __init__(self, w, h, title="c64 draw"):
    """Generates and shows a pygame window.
    
    :param w: window width
    :param h: window height
    """
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
    for event in pygame.event.get():
      if event.type == pygame.locals.QUIT:
        self.show = False
      if event.type == pygame.locals.KEYDOWN:
        if event.key == pygame.locals.K_ESCAPE:
          self.show = False




# --- Memory class --------------------------------------------------
class Memory:
  """The representation of a c64 memory."""

  def __init__(self, data=None):
    """Constructor
    
    Assigns the given data. If no data is given, the data (memory)
    is initialiased with zeros.
    
    :param data: The memory data (should be 65536 bytes long) 
    """
    self.data = data
    if self.data==None:
      self.data = [0]*(65536)

  
  def load(self, fileName):
    """Loads the given files as a memory dump.
    
    Reads the first two bytes as destination (starting address).
    Reads the reminder starting at this address, the rest of the memory
    is filled with zeros.
    
    Loading assures that the memory is complete (is 65536 bytes long)
    
    :param fileName: The file to load
     
    TODO: check destination byte order (not spent a thought on it)
    """
    f = open(fileName, "rb")
    ba = bytearray(f.read())
    startingAddress = ba[0] + ba[1] * 256
    self.data = []
    if startingAddress!=0:
      self.data = [0] * startingAddress
    self.data.extend(list(ba[2:]))
    rest = 65536 - (startingAddress + len(ba) - 2)
    if rest>0: 
        self.data.append([0]*rest)          

  
  def drawAt(self, surface, x, y, cols, fgColor=(255, 255, 255, 255), bgColor=(0, 0, 0, 255)):
    """Draws this memory at the given surface and the given position.
    
    :param surface: The surface to draw this memory to
    :param x: x-offset for drawing
    :param y: y-offset for drawing
    :param cols: the number of (character) columns
    :param fgColor: foreground color given as a tuple of four integers (rgba), may be None
    :param bgColor: background color given as a tuple of four integers (rgba), may be None
    """
    hc = 65536/8/cols # rows in chars
    for yh in range(0, hc):
      for xh in range(0, cols):
        offset = xh*8 + yh*8*cols
        char = Char(self.data[offset:offset+8])
        char.drawAt(surface, x+xh*8, y+yh*8, fgColor, bgColor)

  
  def charAt(self, addr):
    """Returns the eight bytes at the given address as a char
    
    :param addr: The address to read the bytes from
    """
    return Char(self.data[addr:addr+8])




# --- Bitmap class --------------------------------------------------
class Bitmap:
  """The representation of a c64 bitmap."""

  def __init__(self, data=None):
    """Constructor
    
    Assigns the given data. If no data is given, the data (bitmap)
    is initialiased with zeros.
    
    :param data: The bitmap data 
    """
    self.data = data
    if self.data==None:
      self.data = [0]*(40*25*8)
      
  
  def charAt(self, col, row):
    """Returns the Char representation of the character at the given position.

    :param col: The column (in characters) to read the char from 
    :param row: The row (in characters) to read the char from
    """
    off = row*40*8+col*8
    return Char(self.data[off:off+8])

  
  def drawAt(self, surface, x, y, fgColor=(255, 255, 255, 255), bgColor=(0, 0, 0, 255)):
    """Draws this bitmap at the given surface and the given position.

    :param surface: The surface to draw this memory to
    :param x: x-offset for drawing
    :param y: y-offset for drawing
    :param fgColor: foreground color given as a tuple of four integers (rgba), may be None
    :param bgColor: background color given as a tuple of four integers (rgba), may be None
    """
    for yh in range(0, 25):
      for xh in range(0, 40):
        for yl in range(0, 8):
          b = self.data[yh*8*40+xh*8+yl]
          for xl in range(0, 8):
            c = bgColor
            if b&(2**(7-xl))!=0:
              c = fgColor
            if c: surface.set_at((xh*8+xl+x, yh*8+yl+y), c)

  
  def buildFrom(self, surface, x, y):
    """Generates the Bitmap from the given surface, starting at the given position.
    
    Please note that only white pixels are assumed to be set
    
    :param surface: The surface to extract the bitmap from
    :param x: x-offset for reading
    :param y: y-offset for reading
    """
    w = (255,255,255,255)
    for yh in range(0, 25):
      for xh in range(0, 40):
        for yl in range(0, 8):
          v = 0
          for xl in range(0, 8):
            c = 0
            #print surface.get_at((xh*8+xl+x, yh*8+yl+y))
            v = v*2
            if surface.get_at((xh*8+xl+x, yh*8+yl+y))==w:
              c = 1
            v = v+c
          self.data[yh*8*40+xh*8+yl] = v

  
  def fromC64Screen(self, screen, chars):
    """Filss the bitmap using the given screen and character set information
    
    :param screen: The screen to use
    :param chars: The character set to use
    """
    for yh in range(0, 25):
      for xh in range(0, 40):
        char = screen.getCharAt(xh, yh)
        for yl in range(0, 8):
          v = 0
          for xl in range(0, 8):
            c = 0
            v = v*2
            if chars[char].data[yl]&(2**(7-xl)):
              c = 1
            v = v+c
          self.data[yh*8*40+xh*8+yl] = v




# --- Char class ----------------------------------------------------
class Char:
  """A single c64 character"""
  
  def __init__(self, data=None):
    """Constructor, allocates memory.
    
    Assigns the given data. If no data is given, the data (character)
    is initialiased with zeros.
    
    :param data: The character data (should be 8 bytes long) 
    """
    self.data = data
    if self.data==None:
      self.data = [0]*8

  
  def drawAt(self, surface, x, y, fgColor=(255, 255, 255, 255), bgColor=(0, 0, 0, 255)):
    """Draws this character (in hires) at the given surface and the given position.

    :param surface: The surface to draw this memory to
    :param x: x-offset for drawing
    :param y: y-offset for drawing
    :param fgColor: foreground color given as a tuple of four integers (rgba), may be None
    :param bgColor: background color given as a tuple of four integers (rgba), may be None
    """
    for yl in range(0, 8):
      b = self.data[yl]
      for xl in range(0, 8):
        c = bgColor
        if b&(2**(7-xl))!=0:
          c = fgColor
        if c: surface.set_at((xl+x, yl+y), c)

  
  def drawMulticolorAt(self, surface, x, y, fgColor=(255, 255, 255, 255), bgColor=(0, 0, 0, 255), multi1Color=(192, 192, 192, 255), multi2Color=(128, 128, 128, 255)):
    """Draws this character in multicolor at the given surface and the given position.

    :param surface: The surface to draw this memory to
    :param x: x-offset for drawing
    :param y: y-offset for drawing
    :param fgColor: foreground color given as a tuple of four integers (rgba), may be None
    :param bgColor: background color given as a tuple of four integers (rgba), may be None
    :param multi1Color: multi1 color given as a tuple of four integers (rgba), may be None
    :param multi2Color: multi2 color given as a tuple of four integers (rgba), may be None
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


  def same(self, c):
    """Returns whether the given character is same as this one.
    
    :param c: The character to compare this character to
    """
    for i,x in enumerate(self.data):
      if self.data[i]!=c.data[i]:
        return False
    return True


  def writeInto(self, f):
    """Writes this character to a file.
    
    :param f: The file to write this character to
    """
    f.write(bytearray(self.data))


  def inverse(self):
    """Inverses the character"""
    for i,b in enumerate(self.data):
      self.data[i] ^= 255
      
      
# --- Screen class --------------------------------------------------
class Screen:
  """The representation of a c64 screen"""

  def __init__(self, data=None):
    """Constructor, allocates memory.
    
    Assigns the given data. If no data is given, the data (screen)
    is initialiased with zeros.
    
    :param data: The screen data (should be 1000 bytes long) 
    """
    self.data = data
    if self.data==None:
      self.data = [0]*(40*25)


  def getCharAt(self, col, row):
    """Returns the caracter at the given position
    
    :param col: The column to get the character from 
    :param row: The row to get the character from 
    """
    return self.data[col+row*40]


  def setCharAt(self, col, row, char):
    """Sets the given character at the given position
    
    :param col: The column to set the character at 
    :param row: The row to set the character at 
    :param char: The character to set 
    """
    self.data[col+row*40] = char



# --- Helper methods ------------------------------------------------
def open2Write(fileName):
  """Opens a file for writing.
  
  :param fileName: The name of the file to open for writing 
  """
  return open(fileName, "wb")


def saveChars(fileName, pos, chars):
  """Saves the given characters.

  :param fileName: The name of the file to write the given characters to 
  :param pos: unused! 
  :param chars: The characters to save
  
  TODO: remove the pos-parameter 
  """
  fb = open2Write(fileName)
  for c in chars:
    c.writeInto(fb)
  fb.close()

  
def writeByte(f, b):
  """Writes the given byte as a one-byte-bytearray.

  :param f: The file to write the byte to 
  :param b: The byte to write 
  """
  f.write(bytearray([b]))


def writeBytes(f, bs):
  """Writes the given array as a bytearray.
  
  :param f: The file to write the bytes to 
  :param bs: The bytes to write 
  """
  f.write(bytearray(bs))


           