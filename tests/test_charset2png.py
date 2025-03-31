#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for charset2png."""
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
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "c64tools"))
from pathlib import Path
import util
import charset2png


# --- helper functions ----------------------------------------------
def pname(text, path="<DIR>"):
    return util.pname(text, "charset2png", path)


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
    assert pname(captured.out) == ""
    assert pname(captured.err) == """usage: charset2png [-h] [--version] [-o OUTPUT] [-n NUM] [-p PATTERN]
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
    assert pname(captured.out) == """usage: charset2png [-h] [--version] [-o OUTPUT] [-n NUM] [-p PATTERN]
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
    assert pname(captured.err) == ""
    

def test_main_version(capsys):
    """Test behaviour if no arguments are given"""
    try:
        charset2png.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """charset2png 0.20.0
"""
    assert pname(captured.err) == ""


def test_missing_action(capsys, tmp_path):
    """Example test"""
    util.copy(tmp_path, ["ata_1.bin"])
    ret = charset2png.main(["--foreground", "#000000", "--background", "#ffffff", "-n", "64", "-w", "32", "-i", str(tmp_path / "ata_1.bin"), "35328"])
    assert ret==2
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == ""
    assert pname(captured.err) == """charset2png: error: either --show or the output file (--output <FILE>) must be set.
"""
    

def test_example1(capsys, tmp_path):
    """Example test"""
    util.copy(tmp_path, ["ata_1.bin"])
    ret = charset2png.main(["--foreground", "#000000", "--background", "#ffffff", "-o", str(tmp_path / "ata_1_1_1x1.png"), "-n", "64", "-w", "32", "-i", str(tmp_path / "ata_1.bin"), "35328"])
    assert ret==0
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Written 64 chars to <DIR>/ata_1_1_1x1.png
"""
    assert pname(captured.err) == ""
    assert util.fread(tmp_path / "ata_1_1_1x1.png") == util.fread(Path(util.TEST_PATH) / "ata_1_1_1x1.png")


def test_example2(capsys, tmp_path):
    """Example test"""
    util.copy(tmp_path, ["ata_1.bin"])
    ret = charset2png.main(["--foreground", "#000000", "--background", "#ffffff", "-o", str(tmp_path / "ata_1_2_1x2.png"), "-n", "64", "-w", "32", "-i", "-p", "0;64", str(tmp_path / "ata_1.bin"), "51208"])
    assert ret==0
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Written 64 chars to <DIR>/ata_1_2_1x2.png
"""
    assert pname(captured.err) == ""
    assert util.fread(tmp_path / "ata_1_2_1x2.png") == util.fread(Path(util.TEST_PATH) / "ata_1_2_1x2.png")
