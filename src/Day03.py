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

            # then use regex to find any adjacent numbers on the surrounding lines
            # we must look at different positions for the prev and next line, compared to the current one
            prev_iter = re.finditer("[0-9]+", prev_line)
            for match in prev_iter:
               if (match.start() in [symbol_location-1, symbol_location, symbol_location+1]) or (match.end()-1 in [symbol_location-1, symbol_location, symbol_location+1]):
                  sum = sum + int(match.group())

            # check for numbers on the same line, adjacent to the symbol
            curr_iter = re.finditer("[0-9]+", current_line)
            for match in curr_iter:
               if (match.start() in [symbol_location-1, symbol_location+1]) or (match.end()-1 in [symbol_location-1, symbol_location+1]):
                  sum = sum + int(match.group())

            # check for numbers on the next line, adjacent to the symbol
            next_iter = re.finditer("[0-9]+", next_line)
            for match in next_iter:
               if (match.start() in [symbol_location-1, symbol_location, symbol_location+1]) or (match.end()-1 in [symbol_location-1, symbol_location, symbol_location+1]):
                  sum = sum + int(match.group())

   return sum

#####################################################################

def part2(data) -> int:
   
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

      # then, step through the current "middle" line and search for * symbols
      for elem_idx, elem in enumerate(current_line):
         if re.search(r"[\*]", elem) != None:
            symbol_location = elem_idx 
   
            found_numbers = []

            # then use regex to find any adjacent numbers on the surrounding lines
            # we must look at different positions for the prev and next line, compared to the current one
            prev_iter = re.finditer("[0-9]+", prev_line)
            for match in prev_iter:
               if (match.start() in [symbol_location-1, symbol_location, symbol_location+1]) or (match.end()-1 in [symbol_location-1, symbol_location, symbol_location+1]):
                  found_numbers.append(int(match.group()))

            # check for numbers on the same line, adjacent to the symbol
            curr_iter = re.finditer("[0-9]+", current_line)
            for match in curr_iter:
               if (match.start() in [symbol_location-1, symbol_location+1]) or (match.end()-1 in [symbol_location-1, symbol_location+1]):
                  found_numbers.append(int(match.group()))

            # check for numbers on the next line, adjacent to the symbol
            next_iter = re.finditer("[0-9]+", next_line)
            for match in next_iter:
               if (match.start() in [symbol_location-1, symbol_location, symbol_location+1]) or (match.end()-1 in [symbol_location-1, symbol_location, symbol_location+1]):
                  found_numbers.append(int(match.group()))

            # check if we found two numbers for the current *
            if len(found_numbers) == 2:
               sum = sum + (found_numbers[0] * found_numbers[1])

   return sum

#####################################################################

assert part1(get_input("Day03_test.txt")) == 4361
assert part2(get_input("Day03_test.txt")) == 467835

print(part1(get_input("Day03_input.txt")))
print(part2(get_input("Day03_input.txt")))