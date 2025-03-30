#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for charpacker."""
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
import charpacker


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "charpacker").replace("__main__.py", "charpacker")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        charpacker.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.err) == """usage: charpacker [-h] [--version] [-s SCREEN] [-c CHARSET] INPUT_IMAGE
charpacker: error: the following arguments are required: INPUT_IMAGE
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        charpacker.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """usage: charpacker [-h] [--version] [-s SCREEN] [-c CHARSET] INPUT_IMAGE

A char packer.

positional arguments:
  INPUT_IMAGE           the image to load and charpack

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -s SCREEN, --screen-output SCREEN
                        the name of the file to save the screen to
  -c CHARSET, --charset-output CHARSET
                        the name of the file to save the charset to

(c) Daniel Krajzewicz 2016-2025
"""


def test_main_version(capsys):
    """Test behaviour if no arguments are given"""
    try:
        charpacker.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """charpacker 0.18.0
"""
    assert patchName(captured.err) == ""
