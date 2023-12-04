import re
from util import *

def part1(data) -> int:
   
   sum = 0
   prev_line = ""
   current_line = ""
   next_line = ""

   # first, always collect 3 lines to have look at
   for line_no in range(len(data)):
      if line_no == 0:
         prev_line = ""
         current_line = data[line_no]
         next_line = data[line_no+1]
      elif line_no < len(data)-1:
         prev_line = data[line_no-1]
         current_line = data[line_no]
         next_line = data[line_no+1]
      else:
         prev_line = data[line_no-1]
         current_line = data[line_no]
         next_line = ""

      # then, step through the current "middle" line and search for symbols
      for elem_idx, elem in enumerate(current_line):
         if re.search(r"[^a-zA-Z0-9\.]", elem) != None:
            symbol_location = elem_idx

   return sum

#####################################################################

def part2(data) -> int:
   return 0

#####################################################################

assert part1(get_input("Day03_test.txt")) == 4361
assert part2(get_input("Day03_test.txt")) == 0

print(part1(get_input("Day03_input.txt")))
print(part2(get_input("Day03_input.txt")))