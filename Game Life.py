import pygame
import sys
from pygame.color import THECOLORS
import copy
import random

def LenCell(board, x, y):
    i = 0
    if (y-1 >= 0 and x-1 >= 0) and board[y-1][x-1] == 1:        #y+1 < len(board)  y-1 >= 0
        i+=1
    '''if ( and ) and board[y][x] == 1:
        i+=1'''
    if y-1 >= 0 and board[y-1][x] == 1:
        i+=1

    if (y-1 >= 0 and x+1 < len(board[y])) and board[y-1][x+1] == 1:
        i+=1

    if x+1 < len(board[y]) and board[y][x+1] == 1:
        i+=1

    if (y+1 < len(board) and x+1 < len(board[y])) and board[y+1][x+1] == 1:
        i+=1

    if y+1 < len(board) and board[y+1][x] == 1:
        i+=1

    if (y+1 < len(board) and x-1 >= 0) and board[y+1][x-1] == 1:
        i+=1

    if x-1 >= 0 < len(board[y]) and board[y][x-1] == 1:
        i+=1

    return i

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Game Life')
screen.fill('black')

diam = 20
random_flag = 1

simple = [[0] * int(400/diam) for i in range(int(400/diam))]


boardNow = copy.deepcopy(simple)
boardFuture = copy.deepcopy(simple)

mouse_flag = 0
pause_flag = 1
pause_bflag = 0
step_flag = 0
step_bflag = 0
r_bflag = 0

if random_flag == 1:
    for y in range(len(boardNow)):
            for x in range(len(boardNow[y])):
                if random.randint(0, 1) == 1:
                    boardNow[y][x] = 1


while True:
    for y in range(int(400/diam)):
        for x in range(int(400/diam)):
            pygame.draw.rect(screen, 'white', pygame.Rect((x*diam, y*diam), (diam, diam)), width=1)

    if pause_flag == 0 or step_flag == 1:
        for y in range(len(boardNow)):
            for x in range(len(boardNow[y])):
                if boardNow[y][x] == 0:
                    if LenCell(boardNow, x, y) == 3:
                        boardFuture[y][x] = 1
                    else:
                        boardFuture[y][x] = 0
                if boardNow[y][x] == 1:
                    if LenCell(boardNow, x, y) == 2 or LenCell(boardNow, x, y) == 3:
                        boardFuture[y][x] = 1
                    elif LenCell(boardNow, x, y) < 2 or LenCell(boardNow, x, y) > 3:
                        boardFuture[y][x] = 0
        boardNow = copy.deepcopy(boardFuture)
    step_flag = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for y in range(len(boardNow)):
        for x in range(len(boardNow[y])):
            if boardNow[y][x] == 1:
                pygame.draw.rect(screen, 'green', pygame.Rect((x*diam+1, y*diam+1), (diam-1, diam-1)), width=0)
            else:
                pygame.draw.rect(screen, 'black', pygame.Rect((x*diam+1, y*diam+1), (diam-1, diam-1)), width=0)

    if pause_flag == 1:
        pygame.display.set_caption('Game Life - PAUSE')
    else:
        pygame.display.set_caption('Game Life')
    
    if pygame.mouse.get_pressed()[0] == 1 and mouse_flag == 0:
        if boardNow[int(pygame.mouse.get_pos()[1]/diam)][int(pygame.mouse.get_pos()[0]/diam)] == 1:
            boardNow[int(pygame.mouse.get_pos()[1]/diam)][int(pygame.mouse.get_pos()[0]/diam)] = 0
        else:
            boardNow[int(pygame.mouse.get_pos()[1]/diam)][int(pygame.mouse.get_pos()[0]/diam)] = 1
        mouse_flag = 1
    if pygame.mouse.get_pressed()[0] == 0 and mouse_flag == 1:
        mouse_flag = 0

    if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and pause_bflag == 0:
        if pause_flag == 1:
            pause_flag = 0
        else:
            pause_flag = 1
        pause_bflag = 1
    if pygame.key.get_pressed()[pygame.K_SPACE] == 0 and pause_bflag == 1:
        pause_bflag = 0

    if pygame.key.get_pressed()[pygame.K_TAB] == 1 and step_bflag == 0:
        step_flag = 1
        step_bflag = 1
    if pygame.key.get_pressed()[pygame.K_TAB] == 0 and step_bflag == 1:
        step_bflag = 0

    if pygame.key.get_pressed()[pygame.K_r] == 1 and r_bflag == 0:
        if random_flag == 1:
            for y in range(len(boardNow)):
                for x in range(len(boardNow[y])):
                    if random.randint(0, 1) == 1:
                        boardNow[y][x] = 1
        r_bflag = 1
    if pygame.key.get_pressed()[pygame.K_r] == 0 and r_bflag == 1:
        r_bflag = 0
    
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(1)
