Using “m2m2png.py”
==================

“mem2png.py” shows a memory dump, optionally saving it as a png-file. When moving over the window, the memory address below the cursor position will be shown and additionally, the character address, both in decimal as well as in hexadecimal number system. You may use this information for extracting a character set using “charset2png.py”.

The tool has to be started with either one option — the memory dump to load — or the following ones:

* __--file/-f _&lt;MEMORY_DUMP_TO_LOAD&gt;___: the memory dump to load
* __--output/-o _&lt;IMAGE_TO_SAVE&gt;___: the file name to save the memory image to
* __--width/-w _&lt;DISPLAY_WIDTH_IN_CHARACTERS&gt;___: the width of the display in characters (the default is 128)

