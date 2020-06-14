# -*- coding: utf-8 -*-
"""
Write a program (function!) that takes a list and returns 
a new list that contains all the elements of the first list 
minus all the duplicates
"""

a = [1,1,2,3,4,5,5,6,7,12,33,33,42,21,13,12,77,4,6,5]

def no_duplicates(x):
    return list(set(x))

print(no_duplicates(a))