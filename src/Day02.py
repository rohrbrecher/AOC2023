import re
from util import *

def part1(data) -> int:

    sum = 0

    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for line_idx, line in enumerate(data):
        
        # use regex to create lists of the numbers for each color
        reds = re.findall(r"(?<=[,;:] )\d+(?= red)", line)
        greens = re.findall(r"(?<=[,;:] )\d+(?= green)", line)
        blues = re.findall(r"(?<=[,;:] )\d+(?= blue)", line)

        # add game number (line index+1) to total, only if all three colors match the criteria
        if (all(int(x)<=max_cubes["red"] for x in reds)) and \
           (all(int(x)<=max_cubes["green"] for x in greens)) and \
           (all(int(x)<=max_cubes["blue"] for x in blues)):
            sum = sum + (line_idx+1)

    return sum

#####################################################################

def part2(data) -> int:
    sum = 0

    for line_idx, line in enumerate(data):
        
        # use regex to create lists of the numbers for each color
        reds = re.findall(r"(?<=[,;:] )\d+(?= red)", line)
        greens = re.findall(r"(?<=[,;:] )\d+(?= green)", line)
        blues = re.findall(r"(?<=[,;:] )\d+(?= blue)", line)

        # convert the lists to integer for easier calculations
        reds = list(map(int, reds))
        greens = list(map(int, greens))
        blues = list(map(int, blues))

        # multiply the max of each color and add to total
        sum = sum + (max(reds) * max(greens) * max(blues))

    return sum

#####################################################################

assert part1(get_input("Day02_test.txt")) == 8
assert part2(get_input("Day02_test.txt")) == 2286

print(part1(get_input("Day02_input.txt")))
print(part2(get_input("Day02_input.txt")))