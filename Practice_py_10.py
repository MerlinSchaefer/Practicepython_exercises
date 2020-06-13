# -*- coding: utf-8 -*-
"""
This week’s exercise is going to be revisiting an old exercise 
(see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates)
 Make sure your program works on two lists of different sizes. 
 Write this using at least one list comprehension.
"""


import random
a = random.sample(range(1, 25), 7) #create random lists of 7 elements from 1-25
b = random.sample(range(1, 25), 7)
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [num for num in set(a) if num in b] #check for overlapping elements

print(a, "\n", b, "\n", c)