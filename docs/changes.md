ChangeLog for c64tools
======================

&copy; Daniel Krajzewicz 2016&ndash;2025

<https://github.com/dkrajzew/c64tools>

<http://www.krajzewicz.de/docs/c64tools/index.html>


c64tools-0.20.0 (31.03.2025)
----------------------------

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


c64tools-0.18.0 (26.03.2023)
----------------------------

* Working on the documentation


c64tools-0.16.0 (05.02.2023)
----------------------------

* Patched documentation (return types)
* Set proper formatting for [readthedocs](https://c64tools.readthedocs.io/)


c64tools-0.14.0 (04.02.2023)
----------------------------

* installing non-library scripts as console applications
* improving setup.py


c64tools-0.12.0 (02.02.2023)
----------------------------

* patching / extending documentation


c64tools-0.10.0 (28.01.2023)
----------------------------

* using mkdocs for documentation
* added requirements.txt
* moved to BSD license
* improved inline documentation
* removed Travis CI support &mdash; tests will be triggered by github actions


c64tools-0.8 (16.05.2020)
-------------------------

* Adding PyPI and Travis CI support


c64PythonHelper-0.2 (19.04.2020)
--------------------------------

Some updates done when working on an article about c64 fonts. They mainly include extended possibilities to set colors and multicolor support for char-related methods.
