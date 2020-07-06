# -*- coding: utf-8 -*-
"""
In this exercise, we will finish building Hangman.
In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
"""
import random

def pick_word():
    with open("sowpods.txt","r") as f:
        words  = f.readlines()
    return random.choice(words) 




print("Welcome to Hangman. (typing EXIT at any prompt will terminate the game)")
play = "yes"
while play == "yes":
    word = list(pick_word())
    solution = word.copy()
    empty_word = ["_" for x in range(len(word))]
    guessed_letters = []
    game = True
    guesses = 0
    
    letter = input("Guess a letter for the word: ").upper()
    while game == True:
        if letter in guessed_letters:
            letter = ''
            print("You have guessed this letter before. Guessed letters {}".format(guessed_letters))
        elif guesses == 6:
            print("6 incorrect guesses.You lost.")
            print("The word was {}".format("".join(solution)))
            play = input("Try again?(yes/no)").lower()
            game = False
        elif letter in word:
            i = word.index(letter)
            empty_word[i] = letter
            word[i] = "_"
            print("You have {} incorrect guesses left".format(6-guesses))
        elif letter == "EXIT":
            game = False
            play  = "no"
        else: 
             print(" ".join(empty_word))
             if letter is not '':
                guessed_letters.append(letter)
                guesses += 1
                print("You have {} incorrect guesses left".format(6-guesses))
             letter = input("Guess a letter for the word: ").upper()
        if "_" not in empty_word:
            print("You won the word is")
            print("".join(empty_word))
            play = input("Try again? (yes/no)").lower()
            game = False 

