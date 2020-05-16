"""setup.py

This is the setup file for 

 c64tools - Python helper for dealing with Commodore c64 graphics.

(c) Daniel Krajzewicz 2016-2020
daniel@krajzewicz.de
http://www.krajzewicz.de/blog/c64-python-helper.php
https://github.com/dkrajzew/c64tools

Available under GPL 3.0, all rights reserved
"""

# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="c64tools",
    version="0.8",
    author="dkrajzew",
    author_email="d.krajzewicz@gmail.com",
    description="Python helper for dealing with Commodore c64 graphics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dkrajzew/c64tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7, <4',
)

