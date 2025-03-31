# Using “mem2png.py”

“mem2png.py” shows a memory dump, optionally saving it as a png-file. When moving over the window, the memory address below the cursor position will be shown as well as the character address, both in decimal as well as in hexadecimal number systems. You may use this information for extracting a character set using “charset2png.py”.


## Arguments and options

The file to load must be supported. Either **--show** or **--output _&lt;IMAGE_TO_SAVE&gt;_** must be set.

### Arguments

* ***&lt;MEMORY_FILE&gt;***: the memory dump file to load

### Options

* __--show/-s__: show the memory dump
* __--output/-o _&lt;IMAGE_TO_SAVE&gt;___: the name of the output file
* __--width/-w _&lt;DISPLAY_WIDTH_IN_CHARACTERS&gt;___: the width of the window in chars (default: 128)
* __--version__: prints the version information
* __--help/-h__: prints the help screen


Examples
--------

```console
mem2png bb_hex_game.bin 
```

Loads the memory dump “bb_hex_game.bin” and shows it.


```console
mem2png -o bb_game.png bb_hex_game.bin
```

Loads the memory dump “bb_hex_game.bin”, renders it as an image and saves the image to “bb_game.png”. Shows the image, which may look as the following one:

![mem2png example](mem2png1.gif#full "mem2png example")

When hovering over the image, the address information will show the memory address the mouse is currently over.


