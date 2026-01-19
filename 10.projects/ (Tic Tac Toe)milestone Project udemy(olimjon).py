#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 22:38:00 2025

@author: tojiboevolimjon
"""

#!!! MILESTONE PROJECT

#!!!GAME: TIC TAC TOE 


test_board=['0',' ',' ',' ',' ',' ',' ' ,' ',' ',' ']

def display_board(board):
    lines = ""

    lines += "----------------------\n"
    lines += "|      |      |      |\n"
    lines += f"|  {board[7]}   |  {board[8]}   |   {board[9]}  |\n"
    lines += "|      |      |      |\n"
    lines += "----------------------\n"
    lines += "|      |      |      |\n"
    lines += f"|  {board[4]}   |  {board[5]}   |   {board[6]}  |\n"
    lines += "|      |      |      |\n"
    lines += "----------------------\n"
    lines += "|      |      |      |\n"
    lines += f"|  {board[1]}   |  {board[2]}   |   {board[3]}  |\n"
    lines += "|      |      |      |\n"
    lines += "----------------------"

    return lines

player1 = display_board(test_board)
# player1.insert(1,'x')

# print(player1)
# player1=display_board(test_board)


# check winner function 
def check_win(board, mark):
    win_combinations = [
        (7,8,9), (4,5,6), (1,2,3),
        (7,4,1), (8,5,2), (9,6,3),
        (7,5,3), (9,5,1)
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == mark and board[combo[1]] == mark and board[combo[2]] == mark:
            return True
    
    return False


#player input
choose=input("Player1: Do you want to be 'X' or 'O' ?")

#step 2 Start game.
    
answer=input("Are you ready to play ? Enter 'Yes' or 'No'")
   
while answer.lower()!='no':
    if answer.lower()=='yes':
        print("Welcome to Tic Tac Toe game !!!")
        player1=display_board(test_board)
        print(player1)
        number=int(input("Player1,Choose your next position:(1-9)"))  
    
    #player1   
        
    if choose.lower()=='x':
        test_board[number]="X"
        player1=display_board(test_board)
        
        print(player1)
        if check_win(test_board, 'X'):
            print("Player 1 wins!🥳🥳🥳")
            break
       
        
    
        
    
            
        
    else:
        test_board[number]="O"
        
        player1=display_board(test_board)
        
        print(player1)
        if check_win(test_board, 'O'):
            print("Player 1 wins!🥳🥳🥳")
            break
       
        


     #player 2   
        
    number2=int(input("Player2,Choose your next position:(1-9)"))  
    
    if choose.lower()=='x':
        test_board[number2]="O"
        player1=display_board(test_board)
        
        print(player1)
        if check_win(test_board, 'O'):
            print("Player 2 wins!🥳🥳🥳")
            break
    
        
   
        
            
    else:
        test_board[number2]="X"
        
        player1=display_board(test_board)
        
        print(player1)
        if check_win(test_board, 'X'):
            print("Player 2 wins!🥳🥳🥳")
            break
        
    
         
        
        
    
    
    

    
     
    
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
    
        
    
        
        
    
    

    
    

    
            

                       
            
    
    
    