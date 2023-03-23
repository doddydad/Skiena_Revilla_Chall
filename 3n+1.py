# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:35:02 2023

@author: Andrew
"""

# 3n + 1 thingy

import random

def find_sequence_length(n):
    """ find how many steps are required to get to 1 in this algorithm"""
    i = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        elif n %2 == 1:
            n = 3*n + 1
        i += 1
    return i

def main():
    sequence_lengths = []

    # Manual testing
    #i = int(input("start: "))
    #j = int(input("end: "))
    
    # Random testing
    i = random.randint(1, 1000000)
    j = random.randint(i, 1000000)

    for k in range(i, j+1):
        sequence_lengths.append(find_sequence_length(k))

    print(i, j, max(sequence_lengths))

if __name__ == "__main__":
    main()