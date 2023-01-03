import sys
from random import random
import os
import platform
import Enemy

SYSTEM = platform.system()
TEST = True

gameover = False
rows, cols = 10, 10

# Player x, Player y
px, py = 1, 1

# Previous px, Previous py
ppx, ppy = 0, 0

# 0 - EMPTY
# 1 - PLAYER
# 2 - ENEMY

# Generate board as an list [x][y]
board = [[0 for i in range(cols)] for j in range(rows)]
enemies = {}
enemy1 = Enemy(random.randint(5, 9), random.randint(5, 9))


def charpos():
    global ppx, ppy, board
    if (TEST):
        print(f'px = {px}, py = {py}\n')
    board[py][px] = 1
    board[ppy][ppx] = 0
    ppx = px
    ppy = py


def render():
    global rows, cols, board
    # rboard = list(zip(*board[::-1]))
    # rrboard = list(zip(*rboard[::-1]))
    # rrrboard = list(zip(*rboard[::-1]))
    print('----------------------')
    for y in board:
        print(end='|')
        for x in y:
            if (x == 0):
                print(' ', end=' ')
            else:
                print(x, end=' ')
        print(end='|\n')
    print(print('----------------------'), end='\n\n')


def moveup(dist):
    global rows, cols, py, px
    if (py-dist >= 0):
        py -= dist
        return True
    else:
        return False


def movedown(dist):
    global rows, cols, py, px
    if (py+dist < rows):
        py += dist
        return True
    else:
        return False


def moveleft(dist):
    global rows, cols, py, px
    if (px-dist >= 0):
        px -= dist
        return True
    else:
        return False


def moveright(dist):
    global rows, cols, py, px
    if (px+dist < cols):
        px += dist
        return True
    else:
        return False


def clear_console():
    if (SYSTEM == 'Windows'):
        os.system('cls')
    elif (SYSTEM == 'Linux'):
        os.system('clear')


def invalid():
    clear_console()
    render()
    print('Invalid move, try again')


def update():
    charpos()
    clear_console()
    render()


# Initial update
update()


while (not gameover):
    move = input('Inputs are: \nd: down 1\nu: up 1\nl: left 1\nr: right 1\n')

    if (move == 'd'):
        if (movedown(1)):
            update()
        else:
            invalid()
    elif (move == 'u'):
        if (moveup(1)):
            update()
        else:
            invalid()
    elif (move == 'l'):
        if (moveleft(1)):
            update()
        else:
            invalid()
    elif (move == 'r'):
        if (moveright(1)):
            update()
        else:
            invalid()
    elif (move == 'endgame'):
        gameover = True
    else:
        invalid()

    for e in enemies:
        e.move()
