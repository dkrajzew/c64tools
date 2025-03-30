from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper
#
# filemerge tests
#
# (c) Daniel Krajzewicz 2016-2025
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import filemerge


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "filemerge").replace("__main__.py", "filemerge")


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
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """usage: filemerge [-h] [--version] OUTPUT_FILE INPUT_FILE [INPUT_FILE ...]
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
    assert patchName(captured.out) == """usage: filemerge [-h] [--version] OUTPUT_FILE INPUT_FILE [INPUT_FILE ...]

Joins a set of files into one.

positional arguments:
  OUTPUT_FILE  Defines the name of the file to write
  INPUT_FILE   Defines the files to load

options:
  -h, --help   show this help message and exit
  --version    show program's version number and exit

(c) Daniel Krajzewicz 2016-2025
"""

