#!#/usr/bin/python3
import random

roll = random.randint(1,6)
guess = int (input ("Guess the dice roll:\n"))

if guess == roll:
    print("Correct! They rolled a", roll)
else:
    print ("Roll doesn't match to", roll)
