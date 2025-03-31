#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - charpacker - A char packer.

Loads an image and charpacks it. Saves optionally the screen and the character
data. Shows the result.

Arguments
---------

* IMAGE_FILE: the image to load and charpack

Options
-------

* --screen-output/-S OUTPUT_FILE: the name of the file to save the screen at
* --charset-output/-C OUTPUT_FILE: the name of the file to save the charset at
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
import pygame
import structures
from typing import List


# --- methods ---------------------------------------------------------------
# -- charpack
def charpack(bitmap, ret=None):
    """Charpacks a given bitmap

    It is possible to continue a charpacking by supporting a tuple of
    a character list and a screen as the second parameter.

    Args:
        bitmap (Bitmap): the c64 bitmap to charpack
        ret (Tuple[List[Char], Screen]): optional charpack result for continuing

    Returns:
        (Tuple[List[Char], Screen]): The obtained characters and the screen
    """
    if ret==None:
        ret = [[], structures.Screen()]
    for row in range(0, 25):
        for col in range(0, 40):
            found = False
            for j,c in enumerate(ret[0]):
                if bitmap.char_at(col, row).same(c):
                    ret[1].set_char_at(col, row, j)
                    found = True
            if not found:
                ret[0].append(bitmap.char_at(col, row))
                ret[1].set_char_at(col, row, len(ret[0])-1)
    return ret


# -- main
def main(arguments : List[str] = None) -> int:
    """Loads an image file, charpacks it, saves the obtained screen and character
    set and shows the original image, its bitmap representation, and the charpacking
    result.

    Args:
        arguments (List[str]): The command line arguments
    """
    parser = argparse.ArgumentParser(prog="charpacker", description="A char packer.",
        epilog='(c) Daniel Krajzewicz 2016-2025')
    parser.add_argument('--version', action='version', version='%(prog)s 0.20.0')
    parser.add_argument("input", metavar="INPUT_IMAGE", default=None, help="the image to load and charpack")
    parser.add_argument("-S", "--screen-output", dest="screen", default=None, help="the name of the file to save the screen to")
    parser.add_argument("-C", "--charset-output", dest="charset", default=None, help="the name of the file to save the charset to")
    parser.add_argument("-s", "--show", dest="show", action="store_true", help="show the result")
    args = parser.parse_args(arguments)
    ofile_screen = args.screen
    ofile_charset = args.charset

    w = structures.Window(320, 600, "charpacker")
    # load and show the original image
    pic = pygame.image.load(args.input)
    w.screen.blit(pic, (0, 0))
    # build and draw the bitmap
    bo = structures.Bitmap()
    bo.from_surface(w.screen, 0, 0) #
    bo.draw_at(w.screen, 0, 200)
    # charpack
    chars, screen = charpack(bo)
    if len(chars)<257:
        print ("Charpacking succesfull, needed %s chars." % len(chars))
        if ofile_screen:
            print ("saving screen...")
            f = open(ofile_screen, "wb")
            f.write(bytearray(screen.data))
            f.close()
        if ofile_charset:
            print ("saving charset...")
            f = open(ofile_charset, "wb")
            for c in chars:
                f.write(bytearray(c.data))
            f.close()
    else:
        print ("Charpacking failed, needed %s chars." % len(chars))
    if args.show:
        # rebuild the bitmap and show it
        bn = structures.Bitmap()
        bn.from_c64_screen(screen, chars)
        bn.draw_at(w.screen, 0, 400)
        pygame.display.update()
        while ( w.show ):
            w.run()
        pygame.quit()
    return 0
    

# -- main check
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # pragma: no cover

