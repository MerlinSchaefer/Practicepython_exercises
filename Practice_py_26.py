# -*- coding: utf-8 -*-
"""
If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, 
and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents 
a Tic Tac Toe game board, tell me whether anyone has won, and tell 
me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, 
a column, or a diagonal. 
Don’t worry about the case where TWO people have won - 
assume that in every board there will only be one winner.
"""
import numpy as np

game = [[2, 0, 1],
	    [2, 1, 0],
	    [2, 1, 1]]
game_on = True #later use in full game
def check_horizontal(board):
    for row in board:
        if len(set(row))==1:
               print("The winner is Player {}".format(row[0]))
               global game_on #later use in full game
               game_on = False
        

def check_vertical(board):
    board_t = np.transpose(board)
    for row in board_t:
        if len(set(row))==1:
               print("The winner is Player {}".format(row[0]))
               global game_on #later use in full game
               game_on = False
    

def check_diagonal(board):
    diag1 = set([board[0][0],board[1][1],board[2][2]])
    diag2 = set([board[0][2],board[1][1],board[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and board[1][1] != 0:
        print("The winner is Player {}".format(board[1][1]))
   
    
#while game_on == True: #later use in full game
check_horizontal(game)
check_vertical(game)
check_diagonal(game)
             