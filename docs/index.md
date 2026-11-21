[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/c64tools/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/c64tools.svg)](https://pypi.org/project/c64tools/)
![test](https://github.com/dkrajzew/c64tools/actions/workflows/test.yml/badge.svg)
[![Downloads](https://static.pepy.tech/badge/c64tools)](https://pepy.tech/projects/c64tools)
[![Downloads](https://static.pepy.tech/badge/c64tools/week)](https://pepy.tech/projects/c64tools)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/c64tools/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/c64tools?branch=main)
[![Documentation Status](https://readthedocs.org/projects/c64tools/badge/?version=latest)](https://c64tools.readthedocs.io/en/latest/?badge=latest)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)

#

__c64tools__ - Python helper for c64 projects

## Introduction

__c64tools__ is a [Python](https://www.python.org/) library that helps in dealing with Commodore c64 graphics and memory.

The major module is named “[structures.py](api_structures.md)”. It contains classes that represent major c64 artifacts — memory, bitmap, char, screen, etc. These classes usually support loading, drawing, and being extracted from a pygame surface.

In addition, you may find some command line applications which use this module:

* a [charpacker](use_charpacker.md)
* a [c64 memory dump to png renderer](use_mem2png.md)
* a [charset from memory dump extractor](use_charset2png.md)
* a [linking tool](use_filemerge.md)


## Usage

### charpacker

```console
charpacker --show -S screen.bin -C charset.bin logo.png
```

Load an image from “logo.png”, charpack it, and write the resulting screen to “screen.bin” and the resulting charset to “charset.bin”.

### charset2png

```console
charset2png --foreground #000000 --background #ffffff -o bb_1_1x1.png -n 64 -w 32 bb_map.bin 32000
```

Extract the 64 first characters from the character set located at address 32000 within the binary dump file “bb_map.bin”. Set foreground to black, background to white. Render the character set with a column width of 32 characters and writes the result to the image “bb_1_1x1.png”.

### filemerge

```console
filemerge bb_game_disc.bin bb_hex_game.bin bb_prg_game_disc.bin
```

Read the files “bb_hex_game.bin” and “bb_prg_game_disc.bin” into an empty memory to the addresses defined by the first two bytes stored in the files, respectively. Save the resulting memory to “bb_game_disc.bin”.

### mem2png 

```console
mem2png bb_hex_game.bin 
```

Load the memory dump “bb_hex_game.bin” and show it.


## Documentation

The scripts __charpacker__, __mem2png__, __charset2png__, and __filemerge__ are started on the command line. The respective documentation consists of a user manual ([charpacker](use_charpacker.md), [mem2png](use_mem2png.md), [charset2png](use_charset2png.md), [filemerge](use_filemerge.md)).

If you want to contribute, you may check the documentation on [charpacker API](api_charpacker.md), [mem2png API](api_mem2png.md), [charset2png API](api_charset2png.md), and [filemerge API](api_filemerge.md) or visit [c64tools on github](https://github.com/dkrajzew/c64tools) where besides the code you may find the [c64tools issue tracker](https://github.com/dkrajzew/c64tools/issues) or a [discussions about c64tools](https://github.com/dkrajzew/c64tools/discussions) section.

Additional documentation includes a page with relevant [links](links.md) or the [ChangeLog](changes.md). You may find the complete documentation at the [c64tools readthedocs pages](https://c64tools.readthedocs.io/).

## Installation

The current version is 0.20.0. You may install the latest release using pip:

```console
python -m pip install c64tools
```

Or download the [latest release](https://github.com/dkrajzew/c64tools/releases/tag/0.20.0) from github. You may as well clone or download the [c64tools git repository](https://github.com/dkrajzew/c64tools). There is also a page about [installing c64tools](install.md) which lists further options.


## License

__c64tools__ is licensed under the [BSD license](license.md).


## Background

I dealt a lot with the good old c64 in the past, see [my c64 releases](https://www.krajzewicz.de/blog/c64-releases.php). Some years ago, I got in contact with [Crimson/Wrath Designs](https://csdb.dk/scener/?id=15742) who not only brought me back to the scene, but as well motivated me to retry coding on the machine. Yet, as times change, it is possible to use your PC for designing graphics, testing methods, and cross-compiling c64 code. But, this of course needs some libraries.


## Status &amp; Contributing

I am not working actively on __c64tools__. But if you have any issue or idea, I would be very interested. Let me know by [adding an issue](https://github.com/dkrajzew/c64tools/issues) or by dropping me a mail.