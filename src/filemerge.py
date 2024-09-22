#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""c64tools - filemerge - Joins a set of files into one.

Loads the files given and stores them at the designated
(described by the first two bytes) position in memory.
Saves the so obtained memory part, together with the
starting address.

--file/-f: the file(s) to load, separated by a ','
--output/-o: the `name of the file to write

(c) Daniel Krajzewicz 2016-2024
daniel@krajzewicz.de
"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2016-2024, Daniel Krajzewicz"
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
from optparse import OptionParser



# --- methods ---------------------------------------------------------------
# -- main
def main(arguments=None):
    """Initialises an empty memory, loads subsequently the defined files
    to their addresses and writes the memory as occupied by the loaded
    contents.

    Args:
        arguments (List[str]): The command line arguments

    Options
    -------

    * __--file/-f _&lt;FILE&gt;[,&lt;FILE&gt;]*___: the file(s) to load, separated by ‘,’
    * __--output/-o _&lt;FILE&gt;___: the name of the file to write the memory to
    """
    optParser = OptionParser(usage="""usage:\n  %prog <MEMORY_DUMP>\n  %prog [options]""", version="filemerge 0.18.0")
    optParser.add_option("-f", "--file", dest="file", default=None, help="Defines the files to load, separated by a ','")
    optParser.add_option("-o", "--output", dest="output", default=None, help="Defines the name of the file to write")
    options, remaining_args = optParser.parse_args(args=arguments)
    if not options.file:
        optParser.error("no input file(s) given...")
        sys.exit()
    files = options.file.split(",")
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
    fd = open(options.output, "wb")
    print (minAddr)
    fd.write(bytearray([minAddr%256, int(minAddr/256)]))
    fd.write(mem[minAddr:maxAddr])
    fd.close()


# -- main check
if __name__ == "__main__":
    main(sys.argv)
