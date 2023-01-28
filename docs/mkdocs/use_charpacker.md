Using “charpacker.py”
=====================

Charpacking converts a bitmap into a character set and a screen, used either for reducing the overall size, for generating larger fonts, or for allowing other effects, such as changing multi-colours in each raster line.

“__charpacker.py__” loads an image file (.gif, e.g.) and performs the charpacking — indexing same 8×8 pixel characters. It is somehow a Python-version of the original c64 charpacker “[Abraham](https://www.krajzewicz.de/blog/c64-releases.php#abraham1)”.


Options
-------

The tool has to be started with the following options set:

* __--file/-f _&lt;IMAGE_FILE_TO_LOAD&gt;___: the image to charpack
* __--screen-output/-s _&lt;SCREEN_OUTPUT_FILENAME&gt;___: the name of the file to write the screen to
* __--charset-output/-c _&lt;CHARSET_OUTPUT_FILENAME&gt;___: the name of the file to write the charset


Examples
--------

```console
python mem2png.py -f logo.png -s screen.bin -c charset.bin 
```

Loads an image from “logo.png”, charpacks it, and writes the resulting screen to “screen.bin” and the resulting charset to “charset.bin”.


Embedding
---------

Besides using the charpacker as a command line application, you may as well import it in your [Python](https://www.python.org) application and use the charpack method within a script. You may then incrementally fill a character set from a different bitmaps by passing the results of initial steps as the second parameter.
