# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 08:36:29 2020

@author: ms101
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
    
    