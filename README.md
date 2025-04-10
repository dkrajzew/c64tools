[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/c64tools/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/c64tools.svg)](https://pypi.python.org/pypi/c64tools)
![test](https://github.com/dkrajzew/c64tools/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/c64tools)](https://pepy.tech/project/c64tools)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/c64tools/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/c64tools?branch=main)
[![Documentation Status](https://readthedocs.org/projects/c64tools/badge/?version=latest)](https://c64tools.readthedocs.io/en/latest/?badge=latest)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


# c64tools

__c64tools__ is a [Python](https://www.python.org/) library that helps in dealing with Commodore c64 graphics and memory.

You may find more information at http://www.krajzewicz.de/docs/c64tools/index.html.

The major module is named “[c64tools.py](http://www.krajzewicz.de/docs/c64tools/api_c64tools.html)”. It contains classes that represent major c64 artifacts — memory, bitmap, char, screen, etc. These classes usually support loading, drawing, and being extracted from a pygame surface.

In addition, you may find some applications which use this module:

* a [charpacker](http://www.krajzewicz.de/docs/c64tools/use_charpacker.html)
* a [c64 memory dump to png renderer](http://www.krajzewicz.de/docs/c64tools/use_mem2png.html)
* a [charset from memory dump extractor](http://www.krajzewicz.de/docs/c64tools/use_charset2png.html)
* a [linking tool](http://www.krajzewicz.de/docs/c64tools/use_filemerge.html)


# Download and Installation

The __current version__ is [c64tools-0.20.0](https://github.com/dkrajzew/c64tools/releases/tag/0.20.0).

You may __install c64tools__ using

```console
python -m pip install c64tools
```

You may __download a copy or fork the code__ at [c64tools&apos;s github page](https://github.com/dkrajzew/c64tools).

Besides, you may __download the current release__ here:

* [c64tools-0.20.0.zip](https://github.com/dkrajzew/c64tools/archive/refs/tags/0.20.0.zip)
* [c64tools-0.20.0.tar.gz](https://github.com/dkrajzew/c64tools/archive/refs/tags/0.20.0.tar.gz)


# Links

* A complete documentation is located at:
   * <https://c64tools.readthedocs.io/en/latest/> and
   * <https://krajzewicz.de/docs/c64tools/index.html>
* Discussions are open at <https://github.com/dkrajzew/c64tools/discussions>
* The github repository is located at: <https://github.com/dkrajzew/c64tools>
* The issue tracker is located at: <https://github.com/dkrajzew/c64tools/issues>
* The PyPI page is located at: <https://pypi.org/project/c64tools/>


# Changes

## c64tools-0.20.0 (31.03.2025)

* Working on the documentation
* added type hints (where possible)
* replaced OptionParser by ArgumentParser
    * __some of the options have been transferred to arguments__
* changes in __charset2png.py__
    * the option **--quiet** has been replaced by the option **--show**
* changes in __charpacker.py__
    * added the option **--show**
    * short options for **--screen-output** and **--charset-output** are now named **-S** and **-C**, respectively
* added some tests
* **debugged command line execution after install**


# Note

Let me know if you need any further information or advice. I am not actively developing __c64tools__ currently.



