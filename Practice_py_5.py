# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:10:00 2020

@author: ms101
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set(a) & set(b))

print(a)
print(b)
print(c)