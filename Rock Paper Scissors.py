# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:29:44 2020

@author: ANMOL ARORA
"""


import random


moves = ['r', 'p', 's']

player_wins = ['pr', 'sp', 'rs']

wins = 0
loses = 0

while True:
    player_move = input('Your move: ')
    if player_move == 'q':
        break
    computer_move = random.choice(moves)

    print('You: ', player_move)
    print('Me: ', computer_move)

    if player_move == computer_move:
        print('Tie')
    elif player_move + computer_move in player_wins:
        print('You Win!')
        wins += 1
    else:
        print('You Lose!')
        loses += 1

print()
print('GAME OVER!')

print()
print('My Score: ', wins)
print('Computer\'s score: ', loses)

print()
print('See You Next Time')







