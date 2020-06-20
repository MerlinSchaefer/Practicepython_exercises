# -*- coding: utf-8 -*-
"""
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
 
 Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
"""



def draw_row(board_size):
    print(" --- " * board_size)
    print("|    " * (board_size + 1))

if __name__ == "__main__":
    board_size = int(input("What size of board do you want? "))
    
    for i in range(board_size):
        draw_row(board_size)
    print(" --- " * board_size)
             
