# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 08:59:04 2020

@author: ms101
"""


name = input("Please enter your name:")
age = int(input("Please enter your age:"))
copies = int(input("How often do you want me to give you the answer?"))
year_current = 2020
year_hundred = 2020-age+100
print("\n")
for x in range(copies):
    print("Hello {}! You will turn 100 years old in {}.".format(name,year_hundred))
    print("\n")