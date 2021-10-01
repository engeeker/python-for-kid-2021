# loop
# (1) while loop
# (2) for loop

import random  # import a python package called random

num = random.randint(1, 99)  # create a random integer in the range from 1 to 99

chance = 3

# loop
while chance != 0:   # expression is True

    guess = int(input("Please input your guess:"))

    if guess == num:
        print("Congratulations, Corret!")
        break   # break the loop when your guess is correct

    if guess > num:
        print("your guess number is larger than mine")

    if guess < num:
        print("your guess number is smaller than mine")

    chance = chance - 1

print("random number is ", num)