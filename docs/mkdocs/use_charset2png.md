Using “charset2png.py”
======================

“charset2png.py” loads a memory dump, extracts a characters set at the specified position and saves it as an image to the specified file.

You may alter the width of the generated image, given in the number of characters shown besides each other. Further options for limiting the number of characters to extract, for setting the background colour, for optionally inverting the character set, and for defining the height of the space between the lines exist. A generated image may look as given in Figure 3.

The tool has to be started with the following options set:

* __--file/-f _&lt;FILE&gt;___: the memory dump to load
* __--output/-o _&lt;FILE&gt;___: the name of the file to write the character set to
* __--address/-a _&lt;INT&gt;___: the address to extract the character set from
* __--number/-n _&lt;INT&gt;___: the number of characters to extract
* __--pattern/-p _&lt;PATTERN&gt;___: pattern of multi-char character sets
* __--width/-w _&lt;INT&gt;___: the width of the image to generate to build
* __--divider/-d _&lt;INT&gt;___: the height of a divider space between the lines
* __--inverse/-i__: invert the characters
* __--background/-b _&lt;COLOR&gt;___: set the background color, default: #000000
* __--foreground/-c _&lt;COLOR&gt;___: set the foreground color, default: #ffffff
* __--multicolor1/-1 _&lt;COLOR&gt;___: set the multi color 1, default: #c0c0c0
* __--multicolor2/-2 _&lt;COLOR&gt;___: set the multi color 2, default: #808080
* __--multicolor/-m__: use multicolor mode
* __--quiet/-q__: do not show a window, just write the image


Further documentation
---------------------

* There is a !!!
