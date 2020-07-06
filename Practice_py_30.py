# -*- coding: utf-8 -*-
"""
This exercise is Part 1 of 3 of the Hangman exercise series.

In this exercise, the task is to write a function that picks a random word from 
a list of words from the SOWPODS dictionary. 
.
"""

import random

def pick_word():
    with open("sowpods.txt","r") as f:
        words  = f.readlines()
    return random.choice(words) 

print(pick_word())