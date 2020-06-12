# -*- coding: utf-8 -*-
"""
Create a program that asks the user to enter their name and their
age. Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing 
out that many copies of the previous message.
Print out that many copies of the previous message on separate lines.
"""
import datetime as dt
#get user input 
name = input("Please enter your name:")
age = int(input("Please enter your age:"))#convert input string to int
copies = int(input("How often do you want me to give you the answer?"))#convert input string to int
year_current = dt.datetime.now().year #get current year
year_hundred = year_current-age+100 #calculate year in which user turns 100
print("\n")
for x in range(copies): #ouput as often as indicated by user
    print("Hello {}! You will turn 100 years old in {}.".format(name,year_hundred))
    print("\n")