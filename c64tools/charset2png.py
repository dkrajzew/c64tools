#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - charset2png - Extracts a character set at a given address from a given memory dump.

Arguments
---------

* INPUT_FILE: the memory dump to load
* ADDRESS: the address to extract the character set from

Options
-------

* --output/-o FILE: the name of the file to save the charset image into
* --number/-n INT: the number of characters to extract (default: 256)
* --pattern/-p PATTERN: defines the pattern of the character set
* --width/-w WIDTH: sets the width of the image in chars (default: 32)
* --divider/-d INT: sets the height of the dividing empty space between line (default: 4)
* --inverse/-i__: invert the characters
* --background/-b COLOR: sets the background color, default: #000000
* --foreground/-c COLOR: sets the foreground color, default: #ffffff
* --multicolor1/-1 COLOR: sets the multi color 1, default: #c0c0c0
* --multicolor2/-2 COLOR: sets the multi color 2, default: #808080
* --multicolor/-m__: use multicolor mode
* --show/-s__: Show the result after conversion
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
import math
import pygame
import structures
from typing import List


# --- methods ---------------------------------------------------------------
def convert_color(color):
    """Converts a given hex color, optionally lead by a '#', into
        an RGB tuple.

    Args:
        color (string): The hex color string

    Returns:
        (Tuple[int, int, int]): The converted color
    """
    if not color: return None
    color = color.strip("#")
    if len(color)==0: return None
    return tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))


# -- main
def main(arguments : List[str] = None) -> int:
    """Loads the memory dump, extracts the character set saves its display and shows it.

    Args:
        arguments (List[str]): The command line arguments
    """
    parser = argparse.ArgumentParser(prog="charset2png", 
        description="Extracts a character set at a given address from a given memory dump.",
        epilog='(c) Daniel Krajzewicz 2016-2025')
    parser.add_argument('--version', action='version', version='%(prog)s 0.20.0')
    parser.add_argument("input", metavar="INPUT_FILE", default=None, help="the memory dump to load")
    parser.add_argument("address", metavar="ADDRESS", type=int, default=None, help="the address to extract the character set from")
    parser.add_argument("-o", "--output", dest="output", default=None, help="the name of the file to save the charset image into")
    parser.add_argument("-n", "--number", dest="num", type=int, default=256, help="the number of characters to extract (default: 256)")
    parser.add_argument("-p", "--pattern", dest="pattern", default="0", help="defines the pattern of the character set")
    parser.add_argument("-w", "--width", dest="width", type=int, default=32, help="sets the width of the image in chars (default: 32)")
    parser.add_argument("-d", "--divider", dest="divider", type=int, default=4, help="sets the height of the dividing empty space between line (default: 4)")
    parser.add_argument("-i", "--inverse", dest="inverse", action="store_true", help="invert the character set")
    parser.add_argument("-b", "--background", dest="background", default="#000000", help="sets the background color")
    parser.add_argument("-c", "--foreground", dest="foreground", default="#ffffff", help="sets the foreground color")
    parser.add_argument("-1", "--multicolor1", dest="multicolor1", default="#c0c0c0", help="sets the multi color 1")
    parser.add_argument("-2", "--multicolor2", dest="multicolor2", default="#808080", help="sets the multi color 2")
    parser.add_argument("-m", "--multicolor", dest="multicolor", action="store_true", help="use multicolor mode")
    parser.add_argument("-s", "--show", dest="show", action="store_true", help="show the result after conversion")
    args = parser.parse_args(arguments)
    ofile = args.output
    if not args.output and not args.show:
        print ("charset2png: error: either --show or the output file (--output <FILE>) must be set.", file=sys.stderr)
        return 2
    # load the memory dump
    mem = structures.Memory()
    mem.load(args.input)

    # build the surface to fill and save
    pattern = args.pattern.split(";")
    for i,l in enumerate(pattern):
        pattern[i] = pattern[i].split("-")
    rowsPerChar = len(pattern)
    colsPerChar = len(pattern[0])
    width = int(args.width*8)
    height = math.ceil(float(args.num) / float(args.width))
    height = int(height*8*rowsPerChar+(max(1, height)-1)*args.divider)
    s = pygame.Surface((width, height))
    bgColor = convert_color(args.background)
    fgColor = convert_color(args.foreground)
    multi1Color = convert_color(args.multicolor1)
    multi2Color = convert_color(args.multicolor2)
    s.fill(bgColor)
    addr = args.address
    line = 0
    for i in range(0, args.num):
        srcBase = addr + i*8
        dstX = ((i*colsPerChar)%args.width)*8
        dstLine = int(float(i*colsPerChar)/float(args.width))
        dstY = dstLine*rowsPerChar*8 + dstLine*args.divider
        for lp in pattern:
            oX = 0
            for cp in lp:
                src = srcBase + int(cp)*8
                char = mem.char_at(src)
                if args.inverse:
                    char.inverse()
                if args.multicolor: 
                    char.draw_at_multicolor(s, dstX+oX, dstY, fgColor, None, multi1Color, multi2Color)
                else: 
                    char.draw_at(s, dstX+oX, dstY, fgColor, None)
                oX += 8
            dstY += 8
    pygame.image.save(s, args.output)
    print ("Written %s chars to %s" % (args.num, args.output))
    if args.show:
        w = structures.Window(width, height, "charset")
        w.screen.blit(s, (0, 0))
        while (w.show):
            pygame.display.flip()
            w.run()
    pygame.quit()
    return 0


# -- main check
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # pragma: no cover

