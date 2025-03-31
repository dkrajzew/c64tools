#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - test helper."""
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
import shutil
import mem2png
TEST_PATH = os.path.split(__file__)[0]


# --- helper functions ----------------------------------------------
def pname(string, name, path="<DIR>"):
    string = string.replace(str(path), "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", name).replace("pytest", name).replace("optional arguments", "options")


def copy(tmp_path, files):
    for file in files:
        shutil.copy(os.path.join((TEST_PATH), file), str(tmp_path / file))



def fread(filepath):
    with open(filepath, "rb") as fd:
        return fd.read()
