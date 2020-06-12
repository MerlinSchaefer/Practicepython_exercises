# -*- coding: utf-8 -*-
"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""


def StartGame():
    A = "Player A wins!"
    B = "Player B wins!"
    while True:
        choice_A = input("Player A, please choose Rock, Paper or Scissors: ").lower()
        choice_B = input("Player B, please choose Rock, Paper or Scissors: ").lower()
        if choice_A == "rock" and choice_B == "scissors":
            print(A)
            break
        elif choice_A == "scissors" and choice_B == "rock":
            print(B)
            break
        elif choice_A == "scissors" and choice_B == "paper":
            print(A)
            break
        elif choice_A == "paper" and choice_B == "scissors":
            print(B)
            break
        elif choice_A == "paper" and choice_B == "rock":
            print(A)
            break
        elif choice_A == "rock" and choice_B == "paper":
            print(B)
            break
        else:
            print("It's a draw, choose again")

answer = input("Hey! Do you want to play a game of rock, paper scissors? (yes/no)").lower()

if answer == "yes":
    StartGame()
else:
    print("Ok then, see you next time!")

