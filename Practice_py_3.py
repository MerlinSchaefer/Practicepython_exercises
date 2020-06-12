# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 07:51:32 2020

@author: ms101
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
comp_num = int(input("Enter a number to compare the list to:"))

print([num for num in a if num < comp_num])