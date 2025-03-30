#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - filemerge - Joins a set of files into one.

Loads the files given and stores them at the designated
(described by the first two bytes) position in memory.
Saves the so obtained memory part, together with the
starting address.


Arguments
---------

* OUTPUT_FILE: Defines the name of the file to write
* INPUT_FILE(s): Defines the files to load

Options
-------

* -h, --help: show a help screen
* --version: show program's version number and exit
"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2016-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.18.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import sys
import argparse
import configparser
from typing import List


# --- methods ---------------------------------------------------------------
# -- main
def main(arguments : List[str] = None) -> int:
    """Initialises an empty memory, loads subsequently the defined files
    to their addresses and writes the memory as occupied by the loaded
    contents.

    Args:
        arguments (List[str]): The command line arguments
    """
    parser = argparse.ArgumentParser(prog="filemerge", description="Joins a set of files into one.",
        epilog='(c) Daniel Krajzewicz 2016-2025')
    parser.add_argument('--version', action='version', version='%(prog)s 0.18.0')
    parser.add_argument("output", metavar="OUTPUT_FILE", default=None, help="Defines the name of the file to write")
    parser.add_argument("files", metavar="INPUT_FILE", nargs='+', default=None, help="Defines the files to load")
    args = parser.parse_args(arguments)
    if not args.file:
        optParser.error("no input file(s) given...")
        sys.exit()
    files = args.file.split(",")
    mem = bytearray([0]*65536)
    minAddr = 65536
    maxAddr = 0
    for f in files:
        fd = open(f, "rb")
        vals = bytearray(fd.read())
        fd.close()
        addr = vals[0] + 256 * vals[1]
        minAddr = min(minAddr, addr)
        maxAddr = max(maxAddr, addr+len(vals)-2)
        mem = mem[:addr] + bytearray(vals[2:]) + mem[addr+len(vals)-2:]
    fd = open(args.output, "wb")
    print (minAddr)
    fd.write(bytearray([minAddr%256, int(minAddr/256)]))
    fd.write(mem[minAddr:maxAddr])
    fd.close()


# -- main check
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # pragma: no cover
