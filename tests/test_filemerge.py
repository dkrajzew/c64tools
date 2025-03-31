#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for filemerge."""
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
import util
import filemerge


# --- helper functions ----------------------------------------------
def pname(text):
    return util.pname(text, "filemerge")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    try:
        filemerge.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.out) == ""
    assert pname(captured.err) == """usage: filemerge [-h] [--version] OUTPUT_FILE INPUT_FILE [INPUT_FILE ...]
filemerge: error: the following arguments are required: OUTPUT_FILE, INPUT_FILE
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        filemerge.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """usage: filemerge [-h] [--version] OUTPUT_FILE INPUT_FILE [INPUT_FILE ...]

Joins a set of files into one.

positional arguments:
  OUTPUT_FILE  the name of the file to write
  INPUT_FILE   the files to load

options:
  -h, --help   show this help message and exit
  --version    show program's version number and exit

(c) Daniel Krajzewicz 2016-2025
"""
    assert pname(captured.err) == ""


def test_main_version(capsys):
    """Test behaviour if no arguments are given"""
    try:
        filemerge.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """filemerge 0.18.0
"""
    assert pname(captured.err) == ""


