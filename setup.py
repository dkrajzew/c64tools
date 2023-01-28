# ===================================================================
# c64tools - c64 Python helper / setup
#
# (c) Daniel Krajzewicz 2016-2023
# daniel@krajzewicz.de
# http://www.krajzewicz.de/blog/c64-python-helper.php
# https://github.com/dkrajzew/c64tools
# Available under the BSD license.
# ===================================================================

# --- imports -------------------------------------------------------
import setuptools


# --- definitions ---------------------------------------------------
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="c64tools",
  version="0.10.0",
  author="dkrajzew",
  author_email="d.krajzewicz@gmail.com",
  description="c64 Python helper",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/dkrajzew/c64tools",
  packages=setuptools.find_packages(),
  # see https://pypi.org/classifiers/
  classifiers=[
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Intended Audience :: Other Audience",
    "Programming Language :: Python",
    "Topic :: Artistic Software",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Other/Nonlisted Topic",
    "Topic :: Multimedia :: Graphics"
  ],
  python_requires='>=2.7, <4',
)

