#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for charpacker."""
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
import charpacker


# --- helper functions ----------------------------------------------
def pname(text):
    return util.pname(text, "charpacker")


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
    assert pname(captured.out) == ""
    assert pname(captured.err) == """usage: charpacker [-h] [--version] [-S SCREEN] [-C CHARSET] [-s] INPUT_IMAGE
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
    assert pname(captured.out) == """usage: charpacker [-h] [--version] [-S SCREEN] [-C CHARSET] [-s] INPUT_IMAGE

A char packer.

positional arguments:
  INPUT_IMAGE           the image to load and charpack

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -S SCREEN, --screen-output SCREEN
                        the name of the file to save the screen to
  -C CHARSET, --charset-output CHARSET
                        the name of the file to save the charset to
  -s, --show            show the result

(c) Daniel Krajzewicz 2016-2025
"""
    assert pname(captured.err) == ""


def test_main_version(capsys):
    """Test behaviour for version printing"""
    try:
        charpacker.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """charpacker 0.20.0
"""
    assert pname(captured.err) == ""


def test_example1(capsys, tmp_path):
    """Example test"""
    util.copy(tmp_path, ["test.hir.gif"])
    ret = charpacker.main(["--screen-output", str(tmp_path / "scr_out.bin"), "--charset-output", str(tmp_path / "chr_out.bin"), str(tmp_path / "test.hir.gif")])
    assert ret==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """Charpacking succesfull, needed 190 chars.
saving screen...
saving charset...
"""
    assert pname(captured.err) == ""
    assert util.fread(tmp_path / "scr_out.bin") == util.fread(Path(util.TEST_PATH) / "scr_out.bin")
    assert util.fread(tmp_path / "chr_out.bin") == util.fread(Path(util.TEST_PATH) / "chr_out.bin")
