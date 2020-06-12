# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 07:55:19 2020

@author: ms101
"""


input_num = int(input("Please enter a number to get all it's divisors"))

x = list(range(2,input_num+1))

print([num for num in x if input_num % num == 0])