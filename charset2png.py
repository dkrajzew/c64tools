"""charset2png.py

Extracts a character set at a given address from a given memory dump.

:param --file/-f: the memory dump to load
:param --output/-o: the name of the file to write the character set to
:param --address/-a: the address to extract the character set from
:param --number/-n: the number of characters to extract 
:param --pattern/-p: pattern of multi-char character sets
:param --width/-w: the width of the image to generate to build
:param --divider/-d: the height of a divider space between the lines
:param --inverse/-i: invert the characters
:param --background/-b: set the background color (as hexadecimal triple, e.g. #ff0000)

(c) Daniel Krajzewicz 2019
daniel@krajzewicz.de

Available under GPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import pygame
import pygame.gfxdraw
import c64
import sys
import math


# --- methods -------------------------------------------------------
# -- main
def main(args):
  """Loads the memory dump, extracts the character set saves its display and shows it."""
  from optparse import OptionParser
  optParser = OptionParser(usage="""usage:\n  %prog [options]""")
  optParser.add_option("-f", "--file", dest="file", default=None, help="Defines the memory to extract the charset from")
  optParser.add_option("-o", "--output", dest="output", default=None, help="Defines the name of the file to save the charset image at")
  optParser.add_option("-a", "--address", dest="address", type="int", default=None, help="Defines the address to read the character set from")
  optParser.add_option("-n", "--number", dest="num", type="int", default=256, help="Defines how many characters shall be extracted")
  optParser.add_option("-p", "--pattern", dest="pattern", default="0", help="Defines the pattern of the character set")
  optParser.add_option("-w", "--width", dest="width", type="int", default=32, help="Defines the width of the image in chars (default: 32)")
  optParser.add_option("-d", "--divider", dest="divider", default=4, help="Defines the height of the dividing empty space between line (default: 4)")
  optParser.add_option("-i", "--inverse", dest="inverse", action="store_true", help="Inverse the character set")
  optParser.add_option("-b", "--background", dest="background", default="#000000", help="Sets the background")
  options, remaining_args = optParser.parse_args(args=args)
  ifile = options.file
  ofile = options.output
  address = options.address
  if not ifile or not ofile or not address:
    print "Missing options; Please start with --help for advice."
    return
  # load the memory dump
  mem = c64.Memory()
  mem.load(ifile)
                      
  # build the surface to fill and save
  pattern = options.pattern.split(";")
  rowsPerChar = pattern.count('-')+1
  colsPerChar = options.pattern.split('-')[0].count(";")+1
  width = int(options.width*8)
  height = math.ceil(float(options.num) / float(options.width))
  height = int(height*8*rowsPerChar+(max(1, height)-1)*options.divider)
  s = pygame.Surface((width, height))
  options.background = options.background.strip("#")
  s.fill(tuple(int(options.background[i:i+2], 16) for i in (0, 2 ,4)))
  addr = options.address
  line = 0
  for i in range(0, options.num):
    srcBase = addr + i*8
    dstX = ((i*rowsPerChar)%options.width)*8
    dstLine = int(float(i*rowsPerChar)/float(options.width)) 
    dstY = dstLine*rowsPerChar*8 + dstLine*options.divider
    oX = 0
    for p in pattern:
      if p=='-':
        dstY += 8
        oX = 0
        continue  
      src = srcBase + int(p)             
      char = mem.charAt(src)
      if options.inverse:
        char.inverse()
      char.drawAt(s, dstX+oX, dstY)
      oX = oX + 8
  pygame.image.save(s, ofile)
  print "Written %s chars to %s" % (options.num, ofile)  
  w = c64.Window(width, height, "charset")
  w.screen.blit(s, (0, 0))
  while (w.show):
    pygame.display.flip()
    w.run()
  pygame.quit()
                      

# -- main check
if __name__ == "__main__":
  main(sys.argv)
           
           