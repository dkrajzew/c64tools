# ===================================================================
# c64tools - c64 Python helper
#
# Setup module
#
# (c) Daniel Krajzewicz 2016-2025
# daniel@krajzewicz.de
# - https://github.com/dkrajzew/c64tools
# - http://www.krajzewicz.de/docs/c64tools/index.html
# - http://www.krajzewicz.de
#
# Available under the BSD license.
# ===================================================================



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
    license='BSD',
    # add modules
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'charpacker = src.charpacker:main',
            'charset2png = src.charset2png:main',
            'mem2png = src.mem2png:main',
            'filemerge = src.filemerge:main'
        ]
    },
    install_requires = [ "pygame==2.6.0" ],
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Other Audience",
        "Topic :: Artistic Software",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Multimedia :: Graphics"
    ],
    python_requires='>=2.7, <4',
)

