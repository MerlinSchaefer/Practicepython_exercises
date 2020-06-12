# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:15:17 2020

@author: ms101
"""


word = input("Please give a word to check if it is a palindrome: ").lower()
print(word)
if word == word[::-1]:
    print("This is a palindrome!")
else: 
    print("Not a palindrome")