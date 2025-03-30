#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for charset2png."""
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
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import charset2png


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "charset2png").replace("__main__.py", "charset2png")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        charset2png.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """usage: charset2png [-h] [--version] [-o OUTPUT] [-n NUM] [-p PATTERN]
                   [-w WIDTH] [-d DIVIDER] [-i] [-b BACKGROUND]
                   [-c FOREGROUND] [-1 MULTICOLOR1] [-2 MULTICOLOR2] [-m] [-s]
                   INPUT_FILE ADDRESS
charset2png: error: the following arguments are required: INPUT_FILE, ADDRESS
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        charset2png.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """usage: charset2png [-h] [--version] [-o OUTPUT] [-n NUM] [-p PATTERN]
                   [-w WIDTH] [-d DIVIDER] [-i] [-b BACKGROUND]
                   [-c FOREGROUND] [-1 MULTICOLOR1] [-2 MULTICOLOR2] [-m] [-s]
                   INPUT_FILE ADDRESS

Extracts a character set at a given address from a given memory dump.

positional arguments:
  INPUT_FILE            the memory dump to load
  ADDRESS               the address to extract the character set from

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -o OUTPUT, --output OUTPUT
                        the name of the file to save the charset image into
  -n NUM, --number NUM  the number of characters to extract (default: 256)
  -p PATTERN, --pattern PATTERN
                        defines the pattern of the character set
  -w WIDTH, --width WIDTH
                        sets the width of the image in chars (default: 32)
  -d DIVIDER, --divider DIVIDER
                        sets the height of the dividing empty space between
                        line (default: 4)
  -i, --inverse         invert the character set
  -b BACKGROUND, --background BACKGROUND
                        sets the background color
  -c FOREGROUND, --foreground FOREGROUND
                        sets the foreground color
  -1 MULTICOLOR1, --multicolor1 MULTICOLOR1
                        sets the multi color 1
  -2 MULTICOLOR2, --multicolor2 MULTICOLOR2
                        sets the multi color 2
  -m, --multicolor      use multicolor mode
  -s, --show            show the result after conversion

(c) Daniel Krajzewicz 2016-2025
"""


def test_main_version(capsys):
    """Test behaviour if no arguments are given"""
    try:
        charset2png.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """charset2png 0.18.0
"""
    assert patchName(captured.err) == ""
