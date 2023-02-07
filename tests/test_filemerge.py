from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper
#
# filemerge tests
#
# (c) Daniel Krajzewicz 2022-2023
# - daniel@krajzewicz.de
# - http://www.krajzewicz.de
# - https://github.com/dkrajzew/db2qthelp
# - http://www.krajzewicz.de/blog/db2qthelp.php
#
# Available under the BSD license.
# ===================================================================
import sys


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "filemerge").replace("__main__.py", "filemerge")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    import c64tools.filemerge
    try:
        c64tools.filemerge.main([])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """Usage: usage:
  filemerge <MEMORY_DUMP>
  filemerge [options]

filemerge: error: no input file(s) given...
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    import c64tools.filemerge
    try:
        c64tools.filemerge.main(["--help"])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """Usage: usage:
  filemerge <MEMORY_DUMP>
  filemerge [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Defines the files to load, separated by a ','
  -o OUTPUT, --output=OUTPUT
                        Defines the name of the file to write
"""
