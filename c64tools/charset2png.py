from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper / charset2png
#
# Extracts a character set at a given address from a given memory dump.
#
# --file/-f: the memory dump to load
# --output/-o: the name of the file to write the character set to
# --address/-a: the address to extract the character set from
# --number/-n: the number of characters to extract
# --pattern/-p: pattern of multi-char character sets
# --width/-w: the width of the image to generate to build
# --divider/-d: the height of a divider space between the lines
# --inverse/-i: invert the characters
# --background/-b: set the background color, default: #000000
# --foreground/-c: set the foreground color, default: #ffffff
# --multicolor1/-1: Sets the multi color 1, default: #c0c0c0
# --multicolor2/-2: Sets the multi color 2, default: #808080
# --multicolor/-m: Uses multicolor mode
# --quiet/-q: do not show a window, just write the image
#
# (c) Daniel Krajzewicz 2016-2023
# daniel@krajzewicz.de
# http://www.krajzewicz.de/blog/c64-python-helper.php
# https://github.com/dkrajzew/c64tools
# Available under the BSD license.
# ===================================================================


# --- imports -------------------------------------------------------
import pygame
import pygame.gfxdraw
import c64tools
import sys
import math


# --- methods -------------------------------------------------------
def convertColor(color):
    """Converts a given hex color, optionally lead by a '#', into
        an RGB tuple.

    Args:
        color (string): The hex color string

    Returns:
        int[3]: The converted color
    """
    if not color: return None
    color = color.strip("#")
    if len(color)==0: return None
    return tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))


# -- main
def main(args):
    """Loads the memory dump, extracts the character set saves its display and shows it.

    Args:
        args (string[]): The command line arguments

    Options
    -------

    * __--file/-f _&lt;FILE&gt;___: the memory dump to load
    * __--output/-o _&lt;FILE&gt;___: the name of the file to write the character set to
    * __--address/-a _&lt;INT&gt;___: the address to extract the character set from
    * __--number/-n _&lt;INT&gt;___: the number of characters to extract
    * __--pattern/-p _&lt;PATTERN&gt;___: pattern of multi-char character sets
    * __--width/-w _&lt;INT&gt;___: the width of the image to generate to build
    * __--divider/-d _&lt;INT&gt;___: the height of a divider space between the lines
    * __--inverse/-i__: invert the characters
    * __--background/-b _&lt;COLOR&gt;___: set the background color, default: #000000
    * __--foreground/-c _&lt;COLOR&gt;___: set the foreground color, default: #ffffff
    * __--multicolor1/-1 _&lt;COLOR&gt;___: set the multi color 1, default: #c0c0c0
    * __--multicolor2/-2 _&lt;COLOR&gt;___: set the multi color 2, default: #808080
    * __--multicolor/-m__: use multicolor mode
    * __--quiet/-q__: do not show a window, just write the image
    """
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
    optParser.add_option("-b", "--background", dest="background", default="#000000", help="Sets the background color")
    optParser.add_option("-c", "--foreground", dest="foreground", default="#ffffff", help="Sets the foreground color")
    optParser.add_option("-1", "--multicolor1", dest="multicolor1", default="#c0c0c0", help="Sets the multi color 1")
    optParser.add_option("-2", "--multicolor2", dest="multicolor2", default="#808080", help="Sets the multi color 2")
    optParser.add_option("-m", "--multicolor", dest="multicolor", action="store_true", help="Uses multicolor mode")
    optParser.add_option("-q", "--quiet", dest="quiet", action="store_true", help="Do not show a window, just convert")
    options, remaining_args = optParser.parse_args(args=args)
    ifile = options.file
    ofile = options.output
    address = options.address
    if not ifile or not ofile or not address:
        optParser.error("missing options; Please start with --help for advice.")
        return
    # load the memory dump
    mem = c64tools.Memory()
    mem.load(ifile)

    # build the surface to fill and save
    pattern = options.pattern.split(";")
    for i,l in enumerate(pattern):
        pattern[i] = pattern[i].split("-")
    rowsPerChar = len(pattern)
    colsPerChar = len(pattern[0])
    width = int(options.width*8)
    height = math.ceil(float(options.num) / float(options.width))
    height = int(height*8*rowsPerChar+(max(1, height)-1)*options.divider)
    s = pygame.Surface((width, height))
    bgColor = convertColor(options.background)
    fgColor = convertColor(options.foreground)
    multi1Color = convertColor(options.multicolor1)
    multi2Color = convertColor(options.multicolor2)
    s.fill(bgColor)
    addr = options.address
    line = 0
    for i in range(0, options.num):
        srcBase = addr + i*8
        dstX = ((i*colsPerChar)%options.width)*8
        dstLine = int(float(i*colsPerChar)/float(options.width))
        dstY = dstLine*rowsPerChar*8 + dstLine*options.divider
        for lp in pattern:
            oX = 0
            for cp in lp:
                src = srcBase + int(cp)*8
                char = mem.charAt(src)
                if options.inverse:
                    char.inverse()
                if options.multicolor: char.drawMulticolorAt(s, dstX+oX, dstY, fgColor, None, multi1Color, multi2Color)
                else: char.drawAt(s, dstX+oX, dstY, fgColor, None)
                oX += 8
            dstY += 8
    pygame.image.save(s, ofile)
    print ("Written %s chars to %s" % (options.num, ofile))
    if not options.quiet:
        w = c64tools.Window(width, height, "charset")
        w.screen.blit(s, (0, 0))
        while (w.show):
            pygame.display.flip()
            w.run()
    pygame.quit()


# -- main check
if __name__ == "__main__":
  main(sys.argv)

