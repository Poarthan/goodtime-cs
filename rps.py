#!/usr/bin/env python3

import random

choicelist = ["rock", "paper", "scissors"]

comp = random.choice(choicelist)

user = input("Rock, Paper, Scissors, Shoot! \n")
if comp==user:
    print("Tie!")
elif comp=="rock" and user=="paper":
    print("You win!", user, "covers", comp)
elif comp=="rock" and user=="scissors":
    print("You lose!", comp, "smashes", user)
elif comp=="paper" and user=="rock":
    print("You lose!", comp, "covers", user)
elif comp=="paper" and user=="scissors":
    print("You win!", user, "cuts", comp)
elif comp=="scissors" and user=="rock":
    print("You win!", user, "smashes", comp)
elif comp=="scissors" and user=="paper":
    print("You lose!", comp, "cuts", user)
else:
    print("Invalid input. You have not entered rock, paper, or scissors, try again.")

