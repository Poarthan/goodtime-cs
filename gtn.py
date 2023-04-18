#!/usr/bin/env python3

import random

rnum=random.randint(0,100)

for i in range(10):
    guess=int(input("Guess a number between 0 and 100:\n"))
    if guess==rnum:
        print("CORRECT! You win!")
        exit()
    elif guess<rnum:
        print("Too low!")
    else:
        print("Too high!")

print("You LOSE")
