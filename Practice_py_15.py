# -*- coding: utf-8 -*-
"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.
"""


input_str = "My name is Michele"

def reverse_str(string):
    return " ".join(string.split()[::-1])

print(reverse_str(input_str))