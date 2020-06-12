# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:07:53 2020

@author: ms101
"""


number = int(input("Please give me a number."))

if number % 2 != 0:
    print("So you like odd numbers?")
elif number % 4 == 0:
    print("I see you like multiples of 4!")
else:
    print("Cool, you chose an even number!")
    
    
num_one = int(input("Give me a number to check"))
num_two = int(input("What should I divide the first number by?"))

if num_one % num_two == 0:
    print("{} divides evenly into {}".format(num_two,num_one))
else:
    print("{} doesn't divide evenly into {}".format(num_two,num_one))