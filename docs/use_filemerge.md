# Using “filemerge.py”

“filemerge.py” loads specified files into the same “memory”. The parts of the memory occupied by the loaded files are then saved. The destination memory address contained in the first two bytes of the loaded files is considered.


## Arguments and options

### Arguments

* ***&lt;OUTPUT_FILE&gt;***: the name of the file to write
* ***&lt;INPUT_FILE(s)&gt;***: the files to load

### Options


## Examples

```console
filemerge bb_game_disc.bin bb_hex_game.bin bb_prg_game_disc.bin
```

Reads the files “bb_hex_game.bin” and “bb_prg_game_disc.bin” into an empty memory to the addresses defined by their first two bytes. Saves the resulting memory to “bb_game_disc.bin”.