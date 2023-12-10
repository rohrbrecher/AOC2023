import re
from util import *

def part1(data) -> int:
    
    sum = 0
    
    for line in data:
        points = 0
        
        # extract the winning numbers as list
        winning = re.search(r"(?<=: ).*(?= \|)", line).group().split()
        
        # extract the owned numbers as list
        games = re.search(r"(?<=\| ).*", line).group().split()
        
        # search for wins and count the points
        for game in games:
            if game in winning:
                if points == 0: points = 1
                else: points = points * 2

        sum = sum + points

    return sum

#####################################################################

def part2(data) -> int:
    
    sum = 0
    
    cardList = {}

    # create a list to remember the amounts of cards we have so we don't have to duplicate the actual cards
    for line in data:
        cardList[re.search(r"\d{1,3}(?=\: )", line).group()] = 1

    for line in data:
        copyNum = 0
        numWins = 0

        # extract the current cards number
        cardNum = int(re.search(r"\d{1,3}(?=\: )", line).group())

        # look up the amount of cards we have of this number
        cardAmount = cardList[str(cardNum)]

        # extract the winning numbers as list
        winning = re.search(r"(?<=: ).*(?= \|)", line).group().split()
        
        # extract the owned numbers as list
        games = re.search(r"(?<=\| ).*", line).group().split()
        
        # search for wins and count how many of them we have
        for game in games:
            if game in winning:
                numWins = numWins + 1

        # now for each win we must increase the amount we have of the card with the next number
        for win_idx in range(numWins):
            # calc the number of the game we must copy
            copyNum = cardNum + win_idx + 1

            # update the number of cards in the cardList
            if copyNum <= len(data):
                cardList.update({str(copyNum): cardList[str(copyNum)]+cardAmount})

    # iterate through the list and summate all of them
    for value in cardList.values():
        sum = sum + value

    return sum

#####################################################################

assert part1(get_input("Day04_test.txt")) == 13
assert part2(get_input("Day04_test.txt")) == 30

print(part1(get_input("Day04_input.txt")))
print(part2(get_input("Day04_input.txt")))