# Using “charset2png.py”

“charset2png.py” loads a memory dump, extracts a characters set at the specified position and saves it as an image to the specified file.

You may alter the width of the generated image, given in the number of characters shown besides each other. Further options for limiting the number of characters to extract, for setting the background colour, for optionally inverting the character set, and for defining the height of the space between the lines exist.

A special feature is the extraction of 1×2, 2×1, 2×2 or othe character sizes. For this purpose, you have to define how the characters are stored in the memory &mdash; the offsets to the lower / right parts of a character. This is done using the __--pattern__ option. Here, lines are divided using a “;”, characters using a “-”.


## Arguments and Options

### Arguments

* ***&lt;INPUT_FILE&gt;***: the memory dump to load
* ***&lt;ADDRESS&gt;***: the address to extract the character set from

### Options

The tool has to be started with the following options set:

* __--output/-o _&lt;FILE&gt;___: the name of the file to save the charset image into
* __--number/-n _&lt;INT&gt;___: the number of characters to extract (default: 256)
* __--pattern/-p _&lt;PATTERN&gt;___: defines the pattern of the character set
* __--width/-w _&lt;INT&gt;___: sets the width of the image in chars (default: 32)
* __--divider/-d _&lt;INT&gt;___: sets the height of the dividing empty space between line (default: 4)
* __--inverse/-i__: invert the character set
* __--background/-b _&lt;COLOR&gt;___: sets the background color, default: #000000
* __--foreground/-c _&lt;COLOR&gt;___: sets the foreground color, default: #ffffff
* __--multicolor1/-1 _&lt;COLOR&gt;___: sets the multi color 1, default: #c0c0c0
* __--multicolor2/-2 _&lt;COLOR&gt;___: sets the multi color 2, default: #808080
* __--multicolor/-m__: use multicolor mode
* __--show/-s__: show the result after conversion
* __--version__: prints the version information
* __--help/-h__: prints the help screen


## Examples

```console
charset2png --foreground #000000 --background #ffffff -o bb_1_1x1.png -n 64 -w 32 bb_map.bin 32000
```

Extracts the 64 first characters from the character set located at address 32000 within the binary dump file “bb_map.bin”. Sets foreground to black, background to white. Renders the character set with a column width of 32 characters and writes the result to the image “bb_1_1x1.png”.

The resulting image (“bb_1_1x1.png”) looks like that:

![BrainBreak 1×1 charset](bb_1_1x1.png#full "BrainBreak 1×1 charset")

```console
charset2png --foreground #000000 --background #ffffff -o nowonder_6_1_2x2.png -n 64 -w 32 -p "0-64;128-192" -i nowonder_6.bin 2048
```

Extracts the 2×2 character set located at address 2048 within the binary dump file “nowonder_6.bin”. The character is stored in a usual way for a c64 2×2 character set: the upper right part of the character has an offset of 64, the lower left part an offset of 128, and the lower right part an offset of 192. Sets foreground to black, background to white. Renders the character set with a column width of 32 characters and writes the result to the image “nowonder_6_1_2x2.png”.

The resulting image (“nowonder_6_1_2x2.png”) looks like that:

![No Wonder 2×2 charset](nowonder_6_1_2x2.png "No Wonder 2×2 charset")


## Further Notes

* I used it for extracting the fonts I&apos;ve made over time, see my blog post on [c64 Font Sizes](https://www.krajzewicz.de/blog/c64-font-sizes.php).

