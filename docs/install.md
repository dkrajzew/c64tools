# Download and Installation

__c64tools__ is a set of [Python](https://www.python.org/) modules and scripts. To run them, you must have [Python](https://www.python.org/) installed. If you have not installed [Python](https://www.python.org/), yet, please read instructions on installing [Python](https://www.python.org/) first (see below).


## Installing c64tools

The current version is [c64tools-0.20.0](https://github.com/dkrajzew/c64tools/releases/tag/0.20.0).

You have different options for installing __c64tools__.

### Installing from PyPi

You may __install c64tools__ using

```console
python -m pip install c64tools
```

You may consider building a virtual environment, first.

You may then run one of the __c64tools__ using 

```console
charpacker
```
```console
mem2png
```
```console
charset2png
```
```console
filemerge
```

This will install __charpacker__, __mem2png__, __charset2png__, and __filemerge__ as scripts that may be directly called on the command line as well as the [Python](https://www.python.org/) module which you may import using ```import c64tools```. The PyPi version only includes the (executable) source code and files needed to run it.

### Cloning the repository

You may __clone the repository__ which is available at [c64tools&apos;s github page](https://github.com/dkrajzew/c64tools).

```console
git clone https://github.com/dkrajzew/c64tools.git
cd c64tools
```

You may then run __c64tools__ using 

```console
python c64tools/charpacker.py
```
```console
python c64tools/mem2png.py
```
```console
python c64tools/charset2png.py
```
```console
python c64tools/filemerge.py
```

Please note that the current repository version may contain an in-between version with new, undescribed, or even buggy behaviour. You should rather use a recent version.

### Download the latest release

Besides, you may __download the current release__ here:

* [c64tools-0.20.0.zip](https://github.com/dkrajzew/c64tools/archive/refs/tags/0.20.0.zip)
* [c64tools-0.20.0.tar.gz](https://github.com/dkrajzew/c64tools/archive/refs/tags/0.20.0.tar.gz)

You will get the complete copy of the repository which you have to decompress. A folder named ```c64tools-0.20.0``` will be generated. __c64tools.py__ is stored in the ```c64tools``` folder.

You may run __c64tools__ using 


```console
python c64tools/charpacker.py
```
```console
python c64tools/mem2png.py
```
```console
python c64tools/charset2png.py
```
```console
python c64tools/filemerge.py
```


## Installing Python

[Python](https://www.python.org/) is an interpreted programming language. For running __c64tools__ and other scripts written in Python you have to install [Python](https://www.python.org/) itself, first.

For installing [Python](https://www.python.org/), use an installer for your system from <https://www.python.org>.

You should as well install **pip**, a package manager for [Python](https://www.python.org/). After installing [Python](https://www.python.org/), you should be able to install **pip** using:

```console
python get-pip.py
```

You may upgrade pip using:

```console
pip install --upgrade pip
```


