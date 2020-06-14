# -*- coding: utf-8 -*-
"""
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""

a = [5,10,15,20,25]

def list_start_end(x):
    return print([x[0],x[-1]])

list_start_end(a)
