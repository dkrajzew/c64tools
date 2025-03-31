#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - mem2png - A c64 memory dump visualiser that can export the dump to an image.

The file to load must be supported. Either --show or --output must be set.

Arguments
---------

* MEMORY_FILE: the memory dump file to load

Options
-------

* --show/-s: show the memory dump
* --output/-o OUTPUT_FILE: the name of the output file
* --width/-w INT: the width of the window in chars (default: 128)
* -h, --help: show a help screen
* --version: show program's version number and exit
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
import argparse
import configparser
import structures
from typing import List


# --- methods ---------------------------------------------------------------
# -- main
def main(arguments : List[str] = None) -> int:
    """Loads the memory dump, saves its display and shows it.

    Args:
        arguments (List[str]): The command line arguments
    """
    import pygame
    # check arguments
    # set defaults
    ifile = None
    ofile = None
    show = False
    xs = 128
    # parse arguments
    if arguments is None:
        arguments = sys.argv[1:]
    if len(arguments)==2:
        ifile = arguments[1]
        show = True
    else:
        parser = argparse.ArgumentParser(prog="mem2png", 
            description="A c64 memory dump visualiser that can export the dump to an image.",
            epilog='(c) Daniel Krajzewicz 2016-2025')
        parser.add_argument('--version', action='version', version='%(prog)s 0.20.0')
        parser.add_argument("input", metavar="MEMORY_FILE", default=None, help="the memory dump file to load")
        parser.add_argument("-s", "--show", dest="show", action="store_true", default=False, help="show the memory dump")
        parser.add_argument("-o", "--output", dest="store", default=None, help="the name of the output file")
        parser.add_argument("-w", "--width", dest="width", type=int, default=128, help="the width of the window in chars (default: 128)")
        args = parser.parse_args(arguments)
        ifile = args.input
        ofile = args.store
        show = args.show
        xs = args.width
        show = args.show
        if not ofile and not show:
            print ("mem2png: error: --show or the output file (--output <FILE>) must be set.", file=sys.stderr)
            return 2
    # build window and load and draw dump
    INFO = 40
    ys = int(65536/xs)
    xs = xs*8
    w = structures.Window(xs, ys+INFO)
    w.background.fill((0,0,0))
    mem = structures.Memory()
    mem.load(ifile)
    mem.draw_at(w.background, 0, 0, int(xs/8))
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
    if show:
        while (w.show):
            pygame.display.update()
            mx,my = pygame.mouse.get_pos()
            char = (int(mx / 8) + (int(my/8)*int(xs/8))) * 8
            pygame.gfxdraw.filled_polygon(w.screen, [[0,ys+1], [xs,ys+1], [xs,ys+INFO], [0,ys+INFO], [0,ys+1]], (0,0,0))
            textsurface = myfont.render('x=%s, y=%s' % (mx,my), False, (255,255,255))
            w.screen.blit(textsurface, (0, ys))
            textsurface = myfont.render('char address: %s (%x)' % (char, char), False, (255,255,255))
            w.screen.blit(textsurface, (0, ys+16))
            pygame.display.flip()
            w.run()
    pygame.quit()
    return 0


# -- main check
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # pragma: no cover

