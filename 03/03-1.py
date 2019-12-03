#!/usr/bin/env python3
import numpy as np
import scipy.misc as smp
from PIL import Image

size = 24000
global blue
blue = [0,0,254]
global red
red = [254,0,0]
global white
white = [255, 255, 255]
global canvas
canvas = np.zeros((size+1, size+1, 3), dtype=np.uint8)
black = np.zeros((1,1, 3), dtype=np.uint8)

colors = {1: [200,50,50],
          2: [50,50,200],
          3: [50,200,50],
          4: [0,50,200],
          5: [0,50,250],
          6: [50,50,50],
          7: [100,50,50],
          8: [150,50,50]}


def insert_pixel(x, y, color):
    canvas[x, y] = color

def check_pixel(x, y, color):
    if canvas[x, y].all() == black.all():
        return True
    elif canvas[x, y].all() == all(color):
        return True
    else:
        return False

def up(steps, pos, color):
    i = 1
    for i in range(1, steps):
        if check_pixel(pos[0],pos[1]+i, color):
            insert_pixel(pos[0], pos[1]+i, color)
        else:
            insert_pixel(pos[0], pos[1]+i, white)
    r = [pos[0], pos[1]+i]
    return r

def down(steps, pos, color):
    i = 1
    for i in range(1, steps):
        if check_pixel(pos[0],pos[1]-i, color):
            insert_pixel(pos[0], pos[1]-i, color)
        else:
            insert_pixel(pos[0], pos[1]-i, white)
    r = [pos[0], pos[1]-i]
    return r

def left(steps, pos, color):
    i = 1 
    for i in range(1, steps):
        if check_pixel(pos[0]-i,pos[1], color):
            insert_pixel(pos[0]-i, pos[1], color)
        else:
            insert_pixel(pos[0]-i, pos[1], white)
    r = [pos[0]-i, pos[1]]
    return r

def right(steps, pos, color):
    i = 1
    for i in range(1, steps):
        if check_pixel(pos[0]+i,pos[1], color):
            insert_pixel(pos[0]+i, pos[1], color)
        else:
            insert_pixel(pos[0]+i, pos[1], white)
    r = [pos[0]+i, pos[1]]
    return r

def draw_line(direction, steps, pos, color):
    if direction == 'U':
        pos = up(steps, pos, color)
    if direction == 'D':
        pos = down(steps, pos, color)
    if direction == 'L':
        pos = left(steps, pos, color)
    if direction == 'R':
        pos = right(steps, pos, color)
    return pos

def main():
    f = open("input","r")
    
    with open("input") as f:
        line = f.readline()
        print("working...")
        line_num = 1
        while line:
            print(line_num)
            l = line.split(',')
            pos = [size//2,size//2]
            for i in l:
                direction = i[0]
                steps = int(i[1:])
                pos = draw_line(direction, steps, pos, colors[line_num])
            line_num += 1
            pos = [size//2, size//2]
            line = f.readline()
    Image.fromarray(canvas, mode='RGB').save('pic1.png')

if __name__ == '__main__':
    main()
