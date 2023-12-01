from util import *

def part1(data) -> int:
    sum = 0
    
    for line in data:
        num = 0
        first = 0
        second = 0

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

def part2(data) -> int:

    sum = 0
    
    for line in data:
        num = 0
        first = 0
        second = 0

        


        # for elem in line:
        #     if elem.isnumeric() == True:
        #         if first == 0:
        #             first = str(elem)
        #             second = str(elem)
        #         else:
        #             second = str(elem)
                
        num = first + second

        sum = sum + int(num)

    return sum


test_input = get_input("Day01_test.txt")
input = get_input("Day01_input.txt")

assert part1(test_input) == 142
assert part2(test_input) == 0

print(part1(input))
print(part2(input))

# for line in input:
#     print(line)