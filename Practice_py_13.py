# -*- coding: utf-8 -*-
"""
Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate
"""

i = int(input("How many Fibonnaci numbers do you want to be generated? "))

def fibonnaci(n):
    a,b = 0,1
    if n == 1:
        print(a)
    else:
        print(a) ; print(b)
    for i in range(2,n):
        c = a + b
        a,b = b,c
        print(c)
        
fibonnaci(i)