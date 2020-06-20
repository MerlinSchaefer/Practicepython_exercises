# -*- coding: utf-8 -*-
"""
Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, 
and the other .txt file has a list of happy numbers up to 1000.
"""
#from collections import Counter

def filetonumlist(filename):
    
    with open(filename,"r") as file:
        numbers = file.readlines()

    return [int(num.strip("\n")) for num in numbers]


prime_numbers = filetonumlist("prime_numbers.txt")
happy_numbers = filetonumlist("happy_numbers.txt")

print(sorted(list(set(prime_numbers) & set(happy_numbers))))

