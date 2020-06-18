# -*- coding: utf-8 -*-
"""
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) 
and another number. 
The function decides whether or not the given number is inside the list and 
returns (then prints) an appropriate boolean.
"""


def element_search(sorted_list,num):
    print(num in sorted_list)
    
if __name__ == "__main__":
    num_list = [1,2,3,4,5,6,7]
    num = int(input("Enter a number to check: "))
    element_search(num_list, num)