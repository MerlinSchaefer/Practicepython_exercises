# -*- coding: utf-8 -*-
"""
Ask the user for a number and determine whether the number is prime or not.
"""


num = int(input("Please enter a number to check for primality: "))

#x = list(range(2,num)) #create list of numbers <= input_num
def check_prime(num):
    divisors = [i for i in range(2,num) if num % i == 0] #check if any numbers leading up to num are divisors
    
    if not divisors: #if the list is empty no divisors (apart from num itself) are present = prime number
        print("You picked a prime number")
    else:
        print("Not a prime number, your number has the following divisors {}".format(divisors))
        
check_prime(num)