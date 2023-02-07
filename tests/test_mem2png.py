from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper
#
# mem2png tests
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
    return test.replace("pytest", "mem2png").replace("__main__.py", "mem2png")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    import c64tools.mem2png
    try:
        c64tools.mem2png.main([])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """Usage: usage:
  mem2png <MEMORY_DUMP>
  mem2png [options]

mem2png: error: No input file(s) given...
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    import c64tools.mem2png
    try:
        c64tools.mem2png.main(["--help"])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """Usage: usage:
  mem2png <MEMORY_DUMP>
  mem2png [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Defines the memory dump file to load
  -o STORE, --output=STORE
                        Defines the name/path of the output file
  -w WIDTH, --width=WIDTH
                        Defines the width of the window in chars
"""
