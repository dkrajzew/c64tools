from __future__ import print_function
"""mem2png.py

A c64 memory dump visualiser that can export the dump to an image.

Either one argument - the file to load - must be supported or the following options

:param --file/-f: the memory dump to load
:param --output/-o: the image file to write
:param --width/-w: the width of the window / image in characters


(c) Daniel Krajzewicz 2019-2020
daniel@krajzewicz.de
http://www.krajzewicz.de/blog/c64-python-helper.php
https://github.com/dkrajzew/c64tools

Available under GPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import pygame
import pygame.gfxdraw
import c64tools
import sys


# --- methods -------------------------------------------------------
# -- charpack
def charpack(bitmap, ret=None):
  """Charpacks a given bitmap
  
  It is possible to continue a charpacking by supporting a tuple of 
  a character list and a screen as the second parameter.
  
  :param bitmap: the c64 bitmap to charpack 
  :param ret: optional charpack result for continuing 
  """
  if ret==None:
    ret = [[], c64tools.Screen()]
  for row in range(0, 25):
    for col in range(0, 40):
      found = False
      for j,c in enumerate(ret[0]):
        if bitmap.charAt(col, row).same(c):
          ret[1].setCharAt(col, row, j)
          found = True
      if not found:
        ret[0].append(bitmap.charAt(col, row))
        ret[1].setCharAt(col, row, len(ret[0])-1)
  return ret


# -- main
def main(args):
  """Loads an image file, charpacks it, saves the obtained screen and character
  set and shows the original image, its bitmap representation, and the charpacking
  result.
  """
  from optparse import OptionParser
  optParser = OptionParser(usage="""usage:\n  %prog <MEMORY_DUMP>\n  %prog [options]""")
  optParser.add_option("-f", "--file", dest="file", default=None, help="Defines the image to load and charpack")
  optParser.add_option("-s", "--screen-output", dest="screen", default=None, help="Defines the name of the file to save the screen at")
  optParser.add_option("-c", "--charset-output", dest="charset", default=None, help="Defines the name of the file to save the charset at")
  options, remaining_args = optParser.parse_args(args=args)
  ifile = options.file
  ofileScreen = options.screen
  ofileCharset = options.charset
  if not ifile:
    print ("Missing options; Please start with --help for advice.")
    return
  
  w = c64tools.Window(320, 600, "charpacker")
  # load and show the original image
  pic = pygame.image.load(ifile)
  w.screen.blit(pic, (0, 0))
  # build and draw the bitmap
  bo = c64tools.Bitmap()
  bo.fromSurface(w.screen, 0, 0) # 
  bo.drawAt(w.screen, 0, 200)
  # charpack
  chars, screen = charpack(bo)
  if len(chars)<257:
    print ("Charpacking succesfull, needed %s chars." % len(chars))
    if ofileScreen:
      print ("saving screen...")
      f = c64tools.open2Write(ofileScreen)
      f.write(bytearray(screen.data))
      f.close()
    if ofileCharset:
      print ("saving charset...")
      f = c64tools.open2Write(ofileCharset)
      for c in chars:
        f.write(bytearray(c.data))
      f.close()
  else:
    print ("Charpacking failed, needed %s chars." % len(chars))
  # rebuild the bitmap and show it
  bn = c64tools.Bitmap()
  bn.fromC64Screen(screen, chars)
  bn.drawAt(w.screen, 0, 400)
  # show all
  pygame.display.update()
  while ( w.show ):
    w.run()
  pygame.quit()
                      

# -- main check
if __name__ == "__main__":
  main(sys.argv)
           
           