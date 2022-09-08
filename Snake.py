import copy
import random
import pygame
import sys
import time
from pygame.color import THECOLORS
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
col = 3
parts = {1:"4;2", 2:"4;4", 3:"4;3", "head":"4;5"}

apple = "2;1"

flag_apple = False

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Snake')
screen.fill('black')

diam = 20

field = 0
cop = [[0] * int(400/diam) for i in range(int(400/diam))]
new_field = 0

direct = "y;s"   #x-y, w a s d

move_flag = False

new_field = copy.copy(cop)
field = copy.copy(cop)
for y in range(len(new_field)):
    for x in range(len(new_field[y])):
        lone = str(x)+";"+str(y)
        if lone in parts.values():
            if str(get_key(parts, lone)) == "head":
                new_field[y][x] = 2
            else:
                new_field[y][x] = 1
        elif lone == apple:
            new_field[y][x] = 3
        else:
            new_field[y][x] = 0
    
field = copy.copy(new_field)
time_ser = time.time()

while True:
    for y in range(int(400/diam)):
        for x in range(int(400/diam)):
            pygame.draw.rect(screen, 'white', pygame.Rect((x*diam, y*diam), (diam, diam)), width=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(1)

    pygame.display.set_caption('Snake, Score: '+str(col-3))
    
    if (pygame.key.get_pressed()[pygame.K_w] == 1 and direct.split(";")[0] != "y") or (direct.split(";")[1] == "w" and move_flag):
        if int(parts["head"].split(";")[1])-1 == -1 or field[int(parts["head"].split(";")[1])-1][int(parts["head"].split(";")[0])] == 1:
            break
        
        head = parts["head"]
        if field[int(parts["head"].split(";")[1])-1][int(parts["head"].split(";")[0])] != 3:
            parts["head"] = parts["head"].split(";")[0]+";"+str(int(parts["head"].split(";")[1])-1)
            for i in range(1, col):
                parts[i] = parts[i+1]
            parts[col] = head
        else:
            parts["head"] = parts["head"].split(";")[0]+";"+str(int(parts["head"].split(";")[1])-1)
            parts[col+1] = head
            col+=1
            flag_apple = True
        direct = "y;w"
        move_flag = False
    if (pygame.key.get_pressed()[pygame.K_s] == 1 and direct.split(";")[0] != "y") or (direct.split(";")[1] == "s" and move_flag):
        if int(parts["head"].split(";")[1])+1 == len(field) or field[int(parts["head"].split(";")[1])+1][int(parts["head"].split(";")[0])] == 1:
            break
        
        head = parts["head"]
        if field[int(parts["head"].split(";")[1])+1][int(parts["head"].split(";")[0])] != 3:
            parts["head"] = parts["head"].split(";")[0]+";"+str(int(parts["head"].split(";")[1])+1)
            for i in range(1, col):
                parts[i] = parts[i+1]
            parts[col] = head
        else:
            parts["head"] = parts["head"].split(";")[0]+";"+str(int(parts["head"].split(";")[1])+1)
            parts[col+1] = head
            col+=1
            flag_apple = True
        direct = "y;s"
        move_flag = False
    if (pygame.key.get_pressed()[pygame.K_a] == 1 and direct.split(";")[0] != "x") or (direct.split(";")[1] == "a" and move_flag):
        if int(parts["head"].split(";")[0])-1 == -1 or field[int(parts["head"].split(";")[1])][int(parts["head"].split(";")[0])-1] == 1:
            break

        head = parts["head"]
        if field[int(parts["head"].split(";")[1])][int(parts["head"].split(";")[0])-1] != 3:
            parts["head"] = str(int(parts["head"].split(";")[0])-1)+";"+parts["head"].split(";")[1]
            for i in range(1, col):
                parts[i] = parts[i+1]
            parts[col] = head
        else:
            parts["head"] = str(int(parts["head"].split(";")[0])-1)+";"+parts["head"].split(";")[1]
            parts[col+1] = head
            col+=1
            flag_apple = True
        direct = "x;a"
        move_flag = False
    if (pygame.key.get_pressed()[pygame.K_d] == 1 and direct.split(";")[0] != "x") or (direct.split(";")[1] == "d" and move_flag):
        if int(parts["head"].split(";")[0])+1 == len(field) or field[int(parts["head"].split(";")[1])][int(parts["head"].split(";")[0])+1] == 1:
            break

        head = parts["head"]
        if field[int(parts["head"].split(";")[1])][int(parts["head"].split(";")[0])+1] != 3:
            parts["head"] = str(int(parts["head"].split(";")[0])+1)+";"+parts["head"].split(";")[1]
            for i in range(1, col):
                parts[i] = parts[i+1]
            parts[col] = head
        else:
            parts["head"] = str(int(parts["head"].split(";")[0])+1)+";"+parts["head"].split(";")[1]
            parts[col+1] = head
            col+=1
            flag_apple = True
        direct = "x;d"
        move_flag = False
    if flag_apple:
        app = str(random.randint(0, len(field)-1))+";"+str(random.randint(0, len(field)-1))
        while app in parts.values():
            app = str(random.randint(0, 9))+";"+str(random.randint(0, 9))
        apple = copy.copy(app)
        flag_apple = False

    new_field = copy.copy(cop)
    field = copy.copy(cop)
    for y in range(len(new_field)):
        for x in range(len(new_field[y])):
            lone = str(x)+";"+str(y)
            if lone in parts.values():
                if str(get_key(parts, lone)) == "head":
                    new_field[y][x] = 2
                else:
                    new_field[y][x] = 1
            elif lone == apple:
                new_field[y][x] = 3
            else:
                new_field[y][x] = 0
    
    field = copy.copy(new_field)

    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 1:
                pygame.draw.rect(screen, 'green', pygame.Rect((x*diam+1, y*diam+1), (diam-1, diam-1)), width=0)
            elif field[y][x] == 2:
                pygame.draw.rect(screen, 'yellow', pygame.Rect((x*diam+1, y*diam+1), (diam-1, diam-1)), width=0)
            elif field[y][x] == 3:
                pygame.draw.rect(screen, 'red', pygame.Rect((x*diam+1, y*diam+1), (diam-1, diam-1)), width=0)
            else:
                pygame.draw.rect(screen, 'black', pygame.Rect((x*diam+1, y*diam+1), (diam-1, diam-1)), width=0)
    if time.time()-time_ser >= 0.3:
        move_flag = True
        time_ser = time.time()
    time.sleep(0.1)
while True:
    pygame.display.set_caption("Snake, Score: "+str(col-3)+"                   You Die!")
    for y in range(int(400/diam)):
        for x in range(int(400/diam)):
            pygame.draw.rect(screen, 'white', pygame.Rect((x*diam, y*diam), (diam, diam)), width=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(1)
