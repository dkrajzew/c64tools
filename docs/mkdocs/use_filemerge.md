Using “filemerge.py”
====================

“filemerge.py” loads specified files into the same “memory”. The parts of the memory occupied by the loaded files are then saved. The destination memory address contained in the first two bytes of the loaded files is considered.


Options
-------

The tool has to be started with the following options set:

* __--file/-f _&lt;FILE&gt;[,&lt;FILE&gt;]*___: the file(s) to load, separated by ‘,’
* __--output/-o _&lt;FILE&gt;___: the name of the file to write the memory to


Examples
--------

```console
filemerge -f bb_hex_game.bin,bb_prg_game_disc.bin -o bb_game_disc.bin
```

Reads the files “bb_hex_game.bin” and “bb_prg_game_disc.bin” into an empty memory to the addresses defined by their first two bytes. Saves the resulting memory to “bb_game_disc.bin”.