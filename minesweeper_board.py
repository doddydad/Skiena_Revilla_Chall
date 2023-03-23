# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:49:14 2023

@author: Andrew
"""

# minesweeper generally

import random

def minesweeper(height, length, mines):
    """ generates a board and clues for minesweeper """
    
    # Board generating given variables
    total = height*length
    board = []
    # board = [board.append(".") for _ in range(total)]
    for _ in range(total):
        board.append(".")
    for _ in range(mines):
        i = random.randint(0, total-1)
        if board[i] == ".":
            board[i] = "*"
    board = [board[x:x+length] for x in range(0, total, length)]
    return board


print(minesweeper(3,2,2))