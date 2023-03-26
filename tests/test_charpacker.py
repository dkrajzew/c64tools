from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper
#
# charpacker tests
#
# (c) Daniel Krajzewicz 2016-2023
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================
import sys


# --- helper functions ----------------------------------------------
def patchName(test):
    return test.replace("pytest", "charpacker").replace("__main__.py", "charpacker")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    import c64tools.charpacker
    try:
        c64tools.charpacker.main([])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == """pygame 2.1.2 (SDL 2.0.18, Python 3.8.5)
Hello from the pygame community. https://www.pygame.org/contribute.html\n"""
    assert patchName(captured.err) == """Usage: usage:
  charpacker <MEMORY_DUMP>
  charpacker [options]

charpacker: error: no input file(s) given...
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    import c64tools.charpacker
    try:
        c64tools.charpacker.main(["--help"])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """Usage: usage:
  charpacker <MEMORY_DUMP>
  charpacker [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Defines the image to load and charpack
  -s SCREEN, --screen-output=SCREEN
                        Defines the name of the file to save the screen at
  -c CHARSET, --charset-output=CHARSET
                        Defines the name of the file to save the charset at
"""

