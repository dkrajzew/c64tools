[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/c64tools/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/c64tools.svg)](https://pypi.python.org/pypi/c64tools)
[![Downloads](https://pepy.tech/badge/c64tools)](https://pepy.tech/project/c64tools)
[![Coverage](https://img.shields.io/badge/coverage-43%25-success)](https://img.shields.io/badge/coverage-43%25-success)
[![Documentation Status](https://readthedocs.org/projects/c64tools/badge/?version=latest)](https://c64tools.readthedocs.io/en/latest/?badge=latest)

Introduction
============

__c64tools__ is a [Python](https://www.python.org/) library that helps in dealing with Commodore c64 graphics and memory.

The major module is named “[c64tools.py](api_c64tools.md)”. It contains classes that represent major c64 artifacts — memory, bitmap, char, screen, etc. These classes usually support loading, drawing, and being extracted from a pygame surface.

In addition, you may find some applications which use this module:

* a [charpacker](use_charpacker.md)
* a [c64 memory dump to png renderer](use_mem2png.md)
* a [charset from memory dump extractor](use_charset2png.md)
* a [linking tool](use_filemerge.md)


Background
==========

I dealt a lot with the good old c64, see [my c64 releases](https://www.krajzewicz.de/blog/c64-releases.php). Some years ago, I got in contact with [Crimson/Wrath Designs](https://csdb.dk/scener/?id=15742) who not only brought me back to the scene, but as well motivated me to retry coding on the machine. Yet, as times change, it is possible to use your PC for designing graphics, testing methods, and cross-compiling c64 code. But, this of course needs some libraries.




License
=======

__c64tools__ is licensed under the [BSD license](license.md).

