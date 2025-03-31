#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - tests for mem2png."""
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
import mem2png


# --- helper functions ----------------------------------------------
def pname(text, path="<DIR>"):
    return util.pname(text, "mem2png", path)


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
    assert pname(captured.out) == ""
    assert pname(captured.err) == """usage: mem2png [-h] [--version] [-s] [-o STORE] [-w WIDTH] MEMORY_FILE
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
    assert pname(captured.out) == """usage: mem2png [-h] [--version] [-s] [-o STORE] [-w WIDTH] MEMORY_FILE

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
    assert pname(captured.err) == ""


def test_main_version(capsys):
    """Test behaviour if no arguments are given"""
    try:
        mem2png.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """mem2png 0.20.0
"""
    assert pname(captured.err) == ""


def test_missing_action(capsys, tmp_path):
    """Example test"""
    util.copy(tmp_path, ["ata_1.bin"])
    ret = mem2png.main([str(tmp_path / "ata_1.bin")])
    assert ret==2
    captured = capsys.readouterr()
    assert pname(captured.out) == ""
    assert pname(captured.err) == """mem2png: error: --show or the output file (--output <FILE>) must be set.
"""


def test_example1(capsys, tmp_path):
    """Example test"""
    util.copy(tmp_path, ["ata_1.bin"])
    ret = mem2png.main(["--output", str(tmp_path / "mem1.png"), str(tmp_path / "ata_1.bin")])
    assert ret==0
    captured = capsys.readouterr()
    assert pname(captured.out) == ""
    assert pname(captured.err) == ""
    assert util.fread(tmp_path / "mem1.png") == util.fread(Path(util.TEST_PATH) / "mem1.png")
