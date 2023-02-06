from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper
#
# charpacker tests
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
    assert captured.out.replace("__main__.py", "charpacker.py") == """pygame 2.1.2 (SDL 2.0.18, Python 3.8.5)
Hello from the pygame community. https://www.pygame.org/contribute.html\n"""
    assert captured.err.replace("__main__.py", "charpacker.py") == """Usage: usage:
  pytest <MEMORY_DUMP>
  pytest [options]

pytest: error: no input file(s) given...
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
    assert captured.out.replace("__main__.py", "charpacker.py") == """Usage: usage:
  pytest <MEMORY_DUMP>
  pytest [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Defines the image to load and charpack
  -s SCREEN, --screen-output=SCREEN
                        Defines the name of the file to save the screen at
  -c CHARSET, --charset-output=CHARSET
                        Defines the name of the file to save the charset at
"""

