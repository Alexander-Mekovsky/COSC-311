import sys

def print_board(layout):
    for r in layout:
        for c in r:
            print(c, end = '')
        print()
    print(' ')

def x_move(row, col, layout):
    if(layout[row][col] == ' '):
        layout[row][col] = 'X'
    elif(layout[row][col] != ' '):
        print('Spot already occupied. Please try again: ')
        row, col = loc_input()
        x_move(row, col, layout)
    
def o_move(row, col, layout):
    if(layout[row][col] == ' '):
        layout[row][col] = 'O'
    elif(layout[row][col] != ' '):
        print('Spot already occupied. Please try again: ')
        row, col = loc_input()
        o_move(row, col, layout)
    
def loc_input():
    row = int(input('Input row for move: '))
    while(row != 0 and row != 1 and row != 2):
        row = int(input('Incorrect range. Please try again: '))
    col = int(input('Input col for move: '))
    while(col != 0 and col != 1 and col != 2):
        col = int(input('Incorrect range. Please try again: '))
    row *= 2
    col *= 2
    return row, col

def win_condition(layout, i):
    if(layout[0][0] == i and layout[2][2] == i and layout[4][4] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[0][0] == i and layout[0][2] == i and layout[0][4] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[0][0] == i and layout[2][0] == i and layout[4][0] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[2][0] == i and layout[2][2] == i and layout[2][4] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[4][0] == i and layout[4][2] == i and layout[4][4] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[0][4] == i and layout[2][4] == i and layout[4][4] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[0][4] == i and layout[2][2] == i and layout[4][0] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
    elif(layout[0][2] == i and layout[2][2] == i and layout[4][2] == i):
        print(i + ' Wins!')
        sys.exit('Game Ended')
'''
Old version of win_condition here for reference
def win_condition(layout, player):
    if(layout[0][0] == layout[2][2] == layout[4][4]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[0][0] == layout[0][2] == layout[0][4]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[0][0] == layout[2][0] == layout[4][0]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[2][0] == layout[2][2] == layout[2][4]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[4][0] == layout[4][2] == layout[4][4]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[0][4] == layout[2][4] == layout[4][4]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[0][4] == layout[2][2] == layout[4][0]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
    elif(layout[0][2] == layout[2][2] == layout[4][2]):
        print(player + " Wins! \n")
        sys.exit('Game Ended')
'''
def draw_condition(game):
    print("Draw!")
    sys.exit('Game Ended')
    
layout = [[' ', '|', ' ', '|', ' '], ['-----'], [' ', '|', ' ', '|', ' '], ['-----'], [' ', '|', ' ', '|', ' ']]
print_board(layout)
game = True
moves = 0
while(game == True):
    players = ['X', 'O']
    for i in players:
        print("Player " + str(i) + "'s Turn")
        row, col = loc_input()
        if(i == 'X'):
            x_move(row, col, layout)
        if(i == 'O'):
            o_move(row, col, layout)
        print_board(layout)
        moves += 1
        if(moves >= 5):
            win_condition(layout, i)
        if(moves == 9):
            draw_condition(game)
            
'''
Old version of the main function for reference
    print("Player X's Turn")
    row, col = loc_input()
    x_move(row, col, layout)
    moves += 1
    win_condition(layout)
    if(moves == 9):
        draw_condition()
    print("Player O's Turn")
    row, col = loc_input()
    o_move(row, col, layout)
    moves += 1
    win_condition(layout)
'''

