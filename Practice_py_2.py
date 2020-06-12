# -*- coding: utf-8 -*-
"""
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check  and one number
to divide by. If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""


number = int(input("Please give me a number."))#get input and convert to int

if number % 2 != 0: #check if no remainder if num /2
    print("So you like odd numbers?")
elif number % 4 == 0: #extra one
    print("I see you like multiples of 4!")
else:
    print("Cool, you chose an even number!")
    
# Extra two    
num_one = int(input("Give me a number to check"))
num_two = int(input("What should I divide the first number by?"))

if num_one % num_two == 0:
    print("{} divides evenly into {}".format(num_two,num_one))
else:
    print("{} doesn't divide evenly into {}".format(num_two,num_one))