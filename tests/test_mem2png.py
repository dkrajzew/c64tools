#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for mem2png."""
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
import mem2png


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "mem2png").replace("__main__.py", "mem2png")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        mem2png.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """usage: mem2png [-h] [--version] [-s] [-o STORE] [-w WIDTH] MEMORY_FILE
mem2png: error: the following arguments are required: MEMORY_FILE
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        mem2png.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """usage: mem2png [-h] [--version] [-s] [-o STORE] [-w WIDTH] MEMORY_FILE

A c64 memory dump visualiser that can export the dump to an image.

positional arguments:
  MEMORY_FILE           the memory dump file to load

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -s, --show            show the memory dump
  -o STORE, --output STORE
                        the name of the output file
  -w WIDTH, --width WIDTH
                        the width of the window in chars (default: 128)

(c) Daniel Krajzewicz 2016-2025
"""


def test_main_version(capsys):
    """Test behaviour if no arguments are given"""
    try:
        mem2png.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """mem2png 0.18.0
"""
    assert patchName(captured.err) == ""
