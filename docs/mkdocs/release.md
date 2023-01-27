Release Steps
=============

* check the [ChangeLog](https://github.com/dkrajzew/c64tools/blob/master/docs/mkdocs/changes.md)
* patch the release number and the copyright information in
    * the [README.md](https://github.com/dkrajzew/c64tools/blob/master/README.md) file
    * the blog pages
    * the [setup.py](https://github.com/dkrajzew/c64tools/blob/master/setup.py) file
    * the scripts and tests
* run the tests (run tests/run_tests.bat)
* build the pydoc documentation, copy it to the web pages
* commit changes
* build the github release (tag: &lt;VERSION&gt;, name: c64tools-&lt;VERSION&gt;)
* build the PyPi release using !!!