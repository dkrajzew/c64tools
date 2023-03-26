from __future__ import print_function
# ===================================================================
# c64tools - c64 Python helper
#
# charset2png tests
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
    return test.replace("pytest", "charset2png").replace("__main__.py", "charset2png")


# --- test functions ------------------------------------------------
def test_main_empty(capsys):
    """Test behaviour if no arguments are given"""
    import c64tools.charset2png
    try:
        c64tools.charset2png.main([])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patchName(captured.out) == ""
    assert patchName(captured.err) == """Usage: usage:
  charset2png [options]

charset2png: error: missing options; Please start with --help for advice.
"""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    import c64tools.charset2png
    try:
        c64tools.charset2png.main(["--help"])
        assert False
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patchName(captured.out) == """Usage: usage:
  charset2png [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Defines the memory to extract the charset from
  -o OUTPUT, --output=OUTPUT
                        Defines the name of the file to save the charset image
                        at
  -a ADDRESS, --address=ADDRESS
                        Defines the address to read the character set from
  -n NUM, --number=NUM  Defines how many characters shall be extracted
  -p PATTERN, --pattern=PATTERN
                        Defines the pattern of the character set
  -w WIDTH, --width=WIDTH
                        Defines the width of the image in chars (default: 32)
  -d DIVIDER, --divider=DIVIDER
                        Defines the height of the dividing empty space between
                        line (default: 4)
  -i, --inverse         Inverse the character set
  -b BACKGROUND, --background=BACKGROUND
                        Sets the background color
  -c FOREGROUND, --foreground=FOREGROUND
                        Sets the foreground color
  -1 MULTICOLOR1, --multicolor1=MULTICOLOR1
                        Sets the multi color 1
  -2 MULTICOLOR2, --multicolor2=MULTICOLOR2
                        Sets the multi color 2
  -m, --multicolor      Uses multicolor mode
  -q, --quiet           Do not show a window, just convert
"""

