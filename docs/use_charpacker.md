# Using “charpacker.py”

Charpacking converts a bitmap into a character set and a screen, used either for reducing the overall size, for generating larger fonts, or for allowing other effects, such as changing multi-colours in each raster line.

“__charpacker.py__” loads an image file (.gif, e.g.) and performs the charpacking — indexing same 8×8 pixel characters. It is somehow a Python-version of the original c64 charpacker “[Abraham](https://www.krajzewicz.de/blog/c64-releases.php#abraham1)”.


## Arguments and options

### Arguments

The tool has to be started with the following options set:

* ***&lt;INPUT\_IMAGE&gt;***: the image to load and charpack

### Options

* __--screen-output/-S _&lt;SCREEN_OUTPUT_FILENAME&gt;___: the name of the file to save the screen to
* __--charset-output/-C _&lt;CHARSET_OUTPUT_FILENAME&gt;___: the name of the file to save the charset to
* __--show/-s__: shows the result
* __--version__: prints the version information
* __--help/-h__: prints the help screen


## Examples

```console
charpacker --show -S screen.bin -C charset.bin logo.png
```

Loads an image from “logo.png”, charpacks it, and writes the resulting screen to “screen.bin” and the resulting charset to “charset.bin”.

A window will be shown, similar to the one shown in the following image.

![Charpacker window](charpacker1.gif#full "Charpacker window")

The window shows the loaded image three-wise. 

* First, the loaded image as-is is shown.
* Then, the image converted to b/w is shown.
* Then, the charpacked image is shown.


## Embedding

Besides using the charpacker as a command line application, you may as well import it in your [Python](https://www.python.org) application and use the charpack method within a script. You may then incrementally fill a character set from a different bitmaps by passing the results of initial steps as the second parameter.
