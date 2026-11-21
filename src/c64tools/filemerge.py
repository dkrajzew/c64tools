#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - filemerge - Joins a set of files into one.

Loads the files given and stores them at the designated
(described by the first two bytes) position in memory.
Saves the so obtained memory, together with the
starting address.


Arguments
---------

* OUTPUT_FILE: the name of the file to write
* INPUT_FILE(s): the files to load

Options
-------

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
import sys
import argparse


# --- methods ---------------------------------------------------------------
# -- main
def main(arguments : List[str] = None) -> int:
    """Initialises an empty memory, loads subsequently the defined files
    to their addresses and writes the memory as occupied by the loaded
    contents.

    Args:
        arguments (List[str]): The command line arguments
    """
    parser = argparse.ArgumentParser(prog="filemerge",
        description="Joins a set of files into one.",
        epilog='(c) Daniel Krajzewicz 2016-2025')
    parser.add_argument('--version', action='version', version='%(prog)s 0.20.0')
    parser.add_argument("output", metavar="OUTPUT_FILE", default=None, help="the name of the file to write")
    parser.add_argument("files", metavar="INPUT_FILE", nargs='+', default=None, help="the files to load")
    args = parser.parse_args(arguments)
    mem = bytearray([0]*65536)
    min_addr = 65536
    max_addr = 0
    for f in args.files:
        with open(f, "rb") as fd:
            vals = bytearray(fd.read())
        addr = vals[0] + 256 * vals[1]
        min_addr = min(min_addr, addr)
        max_addr = max(max_addr, addr+len(vals)-2)
        mem = mem[:addr] + bytearray(vals[2:]) + mem[addr+len(vals)-2:]
    with open(args.output, "wb") as fd:
        fd.write(bytearray([min_addr%256, int(min_addr/256)]))
        fd.write(mem[min_addr:max_addr])
    return 0


def script_run() -> int:
    """Execute from command line."""
    sys.exit(main(sys.argv[1:])) # pragma: no cover


# -- main check
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # pragma: no cover
