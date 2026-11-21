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
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
from typing import List
import os
import sys
import argparse
import math
import pygame
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import c64tools.structures as structures


# --- methods ---------------------------------------------------------------
def convert_color(color : str):
    """Converts a given hex color, optionally lead by a '#', into
        an RGB tuple.

    Args:
        color (str): The hex color string

    Returns:
        (Tuple[int, int, int]): The converted color
    """
    if not color:
        return None
    color = color.strip("#")
    if len(color)==0:
        return None
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
    if not args.output and not args.show:
        print ("charset2png: error: either --show or the output file (--output <FILE>) must be set.", file=sys.stderr)
        return 2
    # load the memory dump
    mem = structures.Memory()
    mem.load(args.input)

    # build the surface to fill and save
    pattern = args.pattern.split(";")
    for i,_ in enumerate(pattern):
        pattern[i] = pattern[i].split("-")
    rows_per_char = len(pattern)
    cols_per_char = len(pattern[0])
    width = int(args.width*8)
    height = math.ceil(float(args.num) / float(args.width))
    height = int(height*8*rows_per_char+(max(1, height)-1)*args.divider)
    s = pygame.Surface((width, height))
    bg_color = convert_color(args.background)
    fg_color = convert_color(args.foreground)
    multi_color1 = convert_color(args.multicolor1)
    multi_color2 = convert_color(args.multicolor2)
    s.fill(bg_color)
    addr = args.address
    for i in range(0, args.num):
        src_base = addr + i*8
        dst_x = ((i*cols_per_char)%args.width)*8
        dst_line = int(float(i*cols_per_char)/float(args.width))
        dst_y = dst_line*rows_per_char*8 + dst_line*args.divider
        for lp in pattern:
            x_offset = 0
            for cp in lp:
                src = src_base + int(cp)*8
                char = mem.char_at(src)
                if args.inverse:
                    char.inverse()
                if args.multicolor:
                    char.draw_at_multicolor(s, dst_x+x_offset, dst_y, fg_color, None, multi_color1, multi_color2)
                else:
                    char.draw_at(s, dst_x+x_offset, dst_y, fg_color, None)
                x_offset += 8
            dst_y += 8
    pygame.image.save(s, args.output)
    print (f"Written {args.num} chars to '{args.output}'")
    if args.show:
        w = structures.Window(width, height, "charset")
        w.screen.blit(s, (0, 0))
        while w.show:
            pygame.display.flip()
            w.run()
    pygame.quit()
    return 0


def script_run() -> int:
    """Execute from command line."""
    sys.exit(main(sys.argv[1:])) # pragma: no cover


# -- main check
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # pragma: no cover
