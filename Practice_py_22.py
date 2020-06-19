# -*- coding: utf-8 -*-
"""
Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file, 
and print out the results to the screen. 

Extra : take a different txt file (this one had directory names) 
and extract the image category
"""


from collections import Counter


with open("input_exercise_22.txt","r") as file:
    lines = file.readlines()

lines = Counter([line.strip("\n") for line in lines])
print(lines)

#Extra 
print("\n")
print("Extra Exercise:")
with open("extra_exercise_22.txt","r") as file:
    lines = file.readlines()

lines = Counter([line[3:-26] for line in lines]) #this only works because the format stays for more flexible functioning regex may be necessary
print(lines)