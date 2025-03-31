#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""c64tools - c64 Python helper - setup module"""
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


# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="c64tools",
    version="0.20.0",
    author="dkrajzew",
    author_email="d.krajzewicz@gmail.com",
    description="c64 Python helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://c64tools.readthedocs.org/',
    download_url='http://pypi.python.org/pypi/c64tools',
    project_urls={
        'Documentation': 'https://c64tools.readthedocs.io/',
        'Source': 'https://github.com/dkrajzew/c64tools',
        'Tracker': 'https://github.com/dkrajzew/c64tools/issues',
        'Discussions': 'https://github.com/dkrajzew/c64tools/discussions',
    },
    license='BSD-3-Clause',
    # add modules
    packages = ["c64tools", "tests"],
    package_data={
        'tests': ['ata_1.bin', 'chr_out.bin', 'scr_out.bin',
            'mem2.bin', 'mem2_1.bin', 'mem2_2.bin',
            'test.hir.gif', 'ata_1_1_1x1.png', 'ata_1_2_1x2.png',
            'mem1.png' ]
    },
    entry_points = {
        'console_scripts': [
            'charpacker = c64tools.charpacker:main',
            'charset2png = c64tools.charset2png:main',
            'mem2png = c64tools.mem2png:main',
            'filemerge = c64tools.filemerge:main'
        ]
    },
    install_requires = [ "pygame==2.6.0" ],
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Other Audience",
        "Topic :: Artistic Software",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Multimedia :: Graphics"
    ],
    python_requires='>=3, <4',
)

