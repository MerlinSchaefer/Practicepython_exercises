# -*- coding: utf-8 -*-
"""
Create a program that will play the “cows and bulls” game with the user. 
The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

"""
import random


def checknumber(rand_num,num):
    cows = 0
    bulls = 0
    num, rand_num = ([int(d) for d in str(num)],[int(d) for d in str(rand_num)])
    for i,j in zip(num, rand_num):
        if i == j:
            cows += 1
        elif i != j and i in rand_num:
            bulls += 1
    return (cows,bulls)
    


if __name__ == "__main__":
    rand_num = random.randint(1000, 9999)
    counter = 0
    print("Welcome to the cows and bulls Game")
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a bull. For every one in the right place, you get a cow.")
    print("The game ends when you get 4 cows!")
    print("Type exit at any prompt to exit.")
    
    while True:
        user_num = input("Please enter a number: ")
        if user_num == "exit":
            break
        cows_bulls = checknumber(rand_num,user_num)
        counter += 1
        print("{} cow(s) ,{} bull(s)".format(cows_bulls[0],cows_bulls[1]))
        if cows_bulls[0] == 4:
            print("4 cows! You guessed the number!")
            print("You took {} guesses".format(counter))
            break
        else:
            print("Not quite right try again.")
    