# -*- coding: utf-8 -*-
"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

# get user input
word = input("Please give a word to check if it is a palindrome: ").lower()
print(word)
if word == word[::-1]: #check if string and reversed string are equal
    print("This is a palindrome!")
else: 
    print("Not a palindrome")