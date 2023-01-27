from __future__ import print_function
"""filemerge.py

Joins a set of files into one.

Loads the files given and stores them at the designated 
(described by the first two bytes) position in memory.
Saves the so obtained memory part, together with the
starting address.

:param --file/-f: the file(s) to load, separated by a ','
:param --output/-o: the `name of the file to write


(c) Daniel Krajzewicz 2020
daniel@krajzewicz.de
http://www.krajzewicz.de/blog/c64-python-helper.php
https://github.com/dkrajzew/c64tools

Available under LGPL 3.0, all rights reserved
"""


# --- imports -------------------------------------------------------
import sys
from optparse import OptionParser



# --- methods -------------------------------------------------------
# -- main
def main(args):
  """Initialises an empty memory, loads subsequently the defined files
  to their addresses and writes the memory as occupied by the loaded
  contents."""
  optParser = OptionParser(usage="""usage:\n  %prog <MEMORY_DUMP>\n  %prog [options]""")
  optParser.add_option("-f", "--file", dest="file", default=None, help="Defines the files to load, separated by a ','")
  optParser.add_option("-o", "--output", dest="output", default=None, help="Defines the name of the file to write")
  options, remaining_args = optParser.parse_args(args=args)
  if not options.file:
    optParser.error("no input file(s) given...")
    sys.exit()
  files = options.file.split(",")
  mem = bytearray([0]*65536)
  minAddr = 65536
  maxAddr = 0
  for f in files:
    fd = open(f, "rb")
    vals = bytearray(fd.read())
    fd.close()
    addr = vals[0] + 256 * vals[1]
    minAddr = min(minAddr, addr)
    maxAddr = max(maxAddr, addr+len(vals)-2)
    mem = mem[:addr] + bytearray(vals[2:]) + mem[addr+len(vals)-2:]
  fd = open(options.output, "wb")
  print (minAddr)
  fd.write(bytearray([minAddr%256, int(minAddr/256)]))
  fd.write(mem[minAddr:maxAddr])
  fd.close()


# -- main check
if __name__ == "__main__":
  main(sys.argv)
 