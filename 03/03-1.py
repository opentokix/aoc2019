#!/usr/bin/env python3
import numpy as np
import scipy.misc as smp
from PIL import Image

size = 24000
global white
white = np.asarray([255, 255, 255], dtype=np.uint8)
global black
black = np.asarray([0, 0, 0], dtype=np.uint8)

global canvas
canvas = np.zeros((size+1, size+1, 3), dtype=np.uint8)


colors = {1: np.asarray([200,50,50], dtype=np.uint8),
          2: np.asarray([75,75,200], dtype=np.uint8),
          3: np.asarray([50,200,50], dtype=np.uint8),
          4: np.asarray([10,50,200], dtype=np.uint8),
          5: np.asarray([10,50,250], dtype=np.uint8),
          6: np.asarray([50,50,50], dtype=np.uint8),
          7: np.asarray([100,50,50], dtype=np.uint8),
          8: np.asarray([150,50,50], dtype=np.uint8)}



def insert_pixel(x, y, color):
    canvas[x, y] = color

def check_pixel(x, y, c):
    if canvas[x, y].all() == black.all():
        return True
    if canvas[x, y].all() == c.all():    
        return True
    else:
        print("canvas: ", canvas[x, y], "color: ", c)
        print("intersect")
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
            print("parsing line: ", line_num)
            l = line.split(',')
            pos = [size//2,size//2]
            for i in l:
                direction = i[0]
                steps = int(i[1:])
                pos = draw_line(direction, steps, pos, colors[line_num])
            line_num += 1
            pos = [size//2, size//2]
            line = f.readline()
    print("Writing image file, might take some time...")
    Image.fromarray(canvas, mode='RGB').save('pic1.png')

if __name__ == '__main__':
    main()
