# -*- coding: utf-8 -*-
"""
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number
"""


input_num = int(input("Please enter a number to get all it's divisors")) #get input convert to int

x = list(range(2,input_num+1)) #create list of numbers <= input_num

print([num for num in x if input_num % num == 0]) #get divisors