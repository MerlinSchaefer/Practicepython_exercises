# -*- coding: utf-8 -*-
"""
Let’s continue building Hangman. In the game of Hangman, 
a clue word is given by the program that the player has to guess, 
letter by letter. 
The player guesses one letter at a time until the entire word has 
been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).

For this exercise, write the logic that asks a player to guess a letter and displays 
letters in the clue word that were guessed correctly. For now, let the player guess 
an infinite number of times until they get the entire word. 
As a bonus, keep track of the letters the player guessed and 
display a different message if the player tries to guess that 
letter again. 
Remember to stop the game when all the letters have been guessed correctly!
"""
if __name__ == "__main__":
    print("Welcome to Hangman. (typing EXIT at any prompt will terminate the game)")
    word = list("EVAPORATE")
    empty_word = ["_" for x in range(len(word))]
    guessed_letters = []
    game = True
   
    letter = input("Guess a letter for the word: ").upper()
    while game == True:
        if letter in guessed_letters:
            letter = ' '
            print("You have guessed this letter before. Guessed letters {}".format(guessed_letters))
              
        elif letter in word:
            i = word.index(letter)
            empty_word[i] = letter
            word[i] = "_"
            if "_" not in empty_word:
                print("You won the word is")
                print("".join(empty_word))
                game = False
        elif letter == "EXIT":
            game  = False
        else: 
             print(" ".join(empty_word))
             if letter is not " ":
                guessed_letters.append(letter)
                letter = input("Guess a letter for the word: ").upper()
            
        