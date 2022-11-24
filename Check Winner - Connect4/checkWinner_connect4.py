#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:42:32 2022

@author: alishanpremani
"""

#Earlier in the course, you implemented a function that could
#find if someone had won a particular game of either tic-tac-
#toe or mancala based on a 2D list or tuple representing the
#current game board.
#
#In this problem, you'll do the same thing, but for the game
#Connect 4. Write a function called check_winner which takes
#as input a 2D list. It should return "X" if there are four
#adjacent "X" values anywhere in the list (row, column,
#diagonal); "O" if there are four adjacent "O" values
#anywhere in the list; and None if there are neither.
#
#Here are the ways Connect-4 is different from tic-tac-toe:
#
# - Connect-4 is played with 6 rows and 7 columns, not 3
#   rows and 3 columns.
# - You must have 4 in a row (or column or diagonal) to win
#   instead of 3.
# - You may only place pieces in the bottom-most empty
#   space in a column (e.g. you "drop" the pieces in the
#   column and they fall to the first empty spot). Note,
#   though, that this shouldn't affect your reasoning.
#
#To keep things simple, we'll still use "X" and "O" to
#represent the players, and None to represent empty spots.
#You may assume there will be only one winner per board,
#no characters besides "X", "O", and None, and you don't
#have to worry about whether the board is actually a
#valid game of Connect 4.
#
#Hints:
# - Don't forget both kinds of diagonals, top-left to
#   bottom-right and bottom-left to top-right.
# - This board is too large to check every possible place
#   for a winner: there are 69 places a player could win.
# - Remember, if you put a negative index in a list,
#   Python "wraps around" and checks the last value. You
#   may have to control for this.
from operator import itemgetter

def unique(list1):
    #convert 4 char list into set, will only take in unique values
    list_set = set(list1) 
    #convert the set to the list
    return list(list_set)

#Write your function here!
def check_winner(grid):
    boolX = 0
    boolY = 0
    #for i, row in enumerate(grid):
        #for j, item in enumerate(row):
            #print(f'a[{i}][{j}]={item} ', end=' ')

    for i in range(0,6): 
        for j in range(0,7):
            
            #traverse 6 rows
            if (j+3) <= 6:
                list1 = grid[i][j:j+4]
                #if unique value is just x or just o, then x or o win respectively
                #print(unique(list1))
                if unique(list1) == ['X']:
                    ##print("row X win")
                    return 'X'
                elif unique(list1) == ['O']:
                    #print("row O win")
                    return 'O'
    
            #traverse 7 columns
            if (i+3) <= 5:
                #print(i)
                allrows = list(map(itemgetter(j),grid))
                list1 = allrows[i:i+4]

                #if unique value is just x or just o, then x or o win respectively
                if unique(list1) == ['X']:
                    #print("col X win")
                    return 'X'
                elif unique(list1) == ['O']:
                    #print("col O win")
                    return 'O'
        
            #traverse diagonal: top-left to bottom-right
            if (i+3)<=5 and (j+3)<=6:
                allrows1 = list(map(itemgetter(j),grid))
                allrows2 = list(map(itemgetter(j+1),grid))
                allrows3 = list(map(itemgetter(j+2),grid))
                allrows4 = list(map(itemgetter(j+3),grid))
                
                num1 = allrows1[i]
                num2 = allrows2[i+1]
                num3 = allrows3[i+2]
                num4 = allrows4[i+3]
                
                list1 = [num1, num2, num3, num4]
                if unique(list1) == ['X']:
                    return 'X'
                elif unique(list1) == ['O']:
                    return 'O'
    
            #traverse diagonal: bottom-left to top-right
            if (i-3)>=0 and (j+3)<=6:
                allrows1 = list(map(itemgetter(j),grid))
                allrows2 = list(map(itemgetter(j+1),grid))
                allrows3 = list(map(itemgetter(j+2),grid))
                allrows4 = list(map(itemgetter(j+3),grid))
                
                num1 = allrows1[i]
                num2 = allrows2[i-1]
                num3 = allrows3[i-2]
                num4 = allrows4[i-3]
                
                list1 = [num1, num2, num3, num4]
                #print("i=" + str(i) + "j=" + str(j))
                #print(list1)
                #list1 = grid[i:i-4][j:j+4]
                if unique(list1) == ['X']:
                    return 'X'
                elif unique(list1) == ['O']:
                    return 'O'
    return None
        
#The code below tests your function on three Connect-4
#boards. Remember, the line breaks are not needed to create
#a 2D tuple; they're used here just for readability.
xwins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         (None, None, None, None, "X" , None, None),
         (None, None, None, "X" , "O" , "O", None),
         (None, "O" , "X" , "X" , "O" , "X", None),
         ("O" , "X" , "O" , "O" , "O" , "X" , "X"))
owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))
nowins =(("X" , "X" , None, None, None, None, None),
         ("O" , "O" , None, None, None, None, None),
         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
         ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
         ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))
     
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))


