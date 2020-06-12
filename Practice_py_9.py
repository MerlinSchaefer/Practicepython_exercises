# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they 
guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random


num = random.randint(1, 9)
counter = 1
while True:
    guess = int(input("Guess which number between 1 and 9 the computer has chosen  "))
    if num == guess:
        print("Great that was the correct number. It took you {} guess(es)".format(counter))
        repeat = input("If you want to exit please type 'exit', if you want to continue press any key  ")
        if repeat == "exit":
            break
    elif num < guess:
        print("That was too high, try again!")
        counter +=1
    else:
        print("Too low, try again!")
        counter +=1
    
    