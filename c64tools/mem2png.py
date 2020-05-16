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
import sys
import pygame
import pygame.gfxdraw
import pygame.image
import c64tools


# --- methods -------------------------------------------------------
# -- main
def main(args):
  """Loads the memory dump, saves its display and shows it."""
  # check arguments
  # set defaults
  ifile = None
  ofile = None
  show = False
  xs = 128
  # parse arguments
  if len(args)==1:
    print ("You have to give the name of the memory dump to load (or use further options)")
    return
  elif len(args)==2:
    ifile = args[1]
    show = True
  else:
    from optparse import OptionParser
    optParser = OptionParser(usage="""usage:\n  %prog <MEMORY_DUMP>\n  %prog [options]""")
    optParser.add_option("-f", "--file", dest="file", default=None, help="Defines the memory dump file to load")
    #optParser.add_option("-s", "--show", dest="show", action="store_true", default=False, help="Show the dump after loading")
    optParser.add_option("-o", "--output", dest="store", default=None, help="Defines the name/path of the output file")
    optParser.add_option("-w", "--width", dest="width", type="int", default=128, help="Defines the width of the window in chars")
    options, remaining_args = optParser.parse_args(args=args)
    ifile = options.file
    ofile = options.store
    #show = options.show
    xs = options.width
    #if not ofile and not show:
    #  print "You should either want to display (--show) or to save (--output) the file"
    #  return

  # build window and load and draw dump
  INFO = 40
  ys = 65536/xs
  xs = xs*8
  w = c64tools.Window(xs, ys+INFO)
  w.background.fill((0,0,0))
  mem = c64tools.Memory()
  mem.load(ifile)
  mem.drawAt(w.background, 0, 0, xs/8)
  pygame.gfxdraw.line(w.background, 0, ys, xs, ys, (255,0,0))
  w.screen.blit(w.background, (0, 0))
  pygame.font.init()
  myfont = pygame.font.SysFont('Arial', 12)
  
  # save if wanted
  if ofile:
    s = pygame.Surface((xs, ys))
    s.blit(w.screen, [0, 0], [0, 0, xs, ys])
    pygame.image.save(s, ofile)
  
  # run the display loop
  while (w.show):
    pygame.display.update()
    mx,my = pygame.mouse.get_pos()
    char = (int(mx / 8) + (int(my/8)*(xs/8))) * 8
    pygame.gfxdraw.filled_polygon(w.screen, [[0,ys+1], [xs,ys+1], [xs,ys+INFO], [0,ys+INFO], [0,ys+1]], (0,0,0))
    textsurface = myfont.render('x=%s, y=%s' % (mx,my), False, (255,255,255))
    w.screen.blit(textsurface, (0, ys))
    textsurface = myfont.render('char address: %s (%x)' % (char, char), False, (255,255,255))
    w.screen.blit(textsurface, (0, ys+16))
    pygame.display.flip()
    w.run()
  pygame.quit()
                      

# -- main check
if __name__ == "__main__":
  main(sys.argv)
           
           