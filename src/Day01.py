from util import *

def part1(data) -> int:
    sum = 0
    
    for line in data:
        num = 0
        first = 0
        second = 0

        # iterate through the line, find the first and last item and store it
        for elem in line:
            if elem.isnumeric() == True:
                if first == 0:
                    first = str(elem)
                    second = str(elem)
                else:
                    second = str(elem)
                
        num = first + second

        sum = sum + int(num)

    return sum

#####################################################################

def part2(data) -> int:

    sum = 0
    
    for line in data:
        num = 0
        first = 0
        second = 0
        lowest_index = -1
        lowest_elem = 150
        low_index_list = []
        highest_index = -1
        highest_elem = 0
        high_index_list = []

        string_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        
        # first, find occurences of each of the "words" within the current line and store them in a list
        for word in string_list:
            low_index_list.append(line.find(word))

        # then walk through the list, find the word which was found first (lowest index) and store its value
        for low_index, low_elem in enumerate(low_index_list):
            if low_elem != -1:
                if low_elem <= lowest_elem:
                    lowest_elem = low_elem
                    lowest_index = low_index
        
        # then insert the actual number in front of the "word"
        if lowest_index != -1:
            line = line[:lowest_elem] + num_list[lowest_index] + line[lowest_elem:]
        
        # now find occurences of each of the words, but starting at the end of the line
        for word in string_list:
            high_index_list.append(line.rfind(word))        

        # again, walk through the list and find the word which was found the rightmost
        for high_index, high_elem in enumerate(high_index_list):
            if high_elem != -1:
                if high_elem >= highest_elem:
                    highest_elem = high_elem
                    highest_index = high_index

        # insert the number in front of the word
        if highest_index != -1:
            line = line[:highest_elem] + num_list[highest_index] + line[highest_elem:]

        # and now we can count the same way as we did for part 1, ignoring all the letters
        for elem in line:
            if elem.isnumeric() == True:
                if first == 0:
                    first = str(elem)
                    second = str(elem)
                else:
                    second = str(elem)
                
        num = first + second

        sum = sum + int(num)

    return sum
#####################################################################

assert part1(get_input("Day01_test.txt")) == 142
assert part2(get_input("Day01_test2.txt")) == 281

print(part1(get_input("Day01_input.txt")))
print(part2(get_input("Day01_input.txt")))