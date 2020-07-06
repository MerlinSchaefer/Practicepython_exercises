# -*- coding: utf-8 -*-
"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
"""


def find_max(x,y,z):
     max_value = 0
     if x > y:
         max_value = x
         if x > z:
             max_value = z
     else:
          if y > z:
             max_value = y
          else:
             max_value = z
     return max_value

print(find_max(1, 2, 3))
print(find_max(4, 4, 1))
print(find_max(2,3,1))
