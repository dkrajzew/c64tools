Release Steps
=============

* check the [ChangeLog](https://github.com/dkrajzew/c64tools/blob/master/docs/mkdocs/changes.md)
* patch the release number and the copyright information in
    * the [setup.py](https://github.com/dkrajzew/c64tools/blob/master/setup.py) file
    * the [install.md](https://github.com/dkrajzew/c64tools/blob/master/docs/mkdocs/install.md) file
    * the [README.md](https://github.com/dkrajzew/c64tools/blob/master/README.md) file
    * the tools
* rerun and patch tests
* commit changes
* build and upload the documentation
    * use the script "___&lt;C64TOOLS&gt;_\docs\build_docs.bat__"
    * copy it to the web pages
* build the github release (tag: ___&lt;VERSION&gt;___, name: __c64tools-_&lt;VERSION&gt;___)
* build the PyPI release using the script "___&lt;C64TOOLS&gt;_\docs\build_release.bat__"
