#!/usr/bin/env python3
import numpy as np
import scipy.misc as smp
from PIL import Image
size = 25000
dists = []
global white
white = np.asarray([255, 255, 255], dtype=np.uint8)
global black
black = np.asarray([0, 0, 0], dtype=np.uint8)

global canvas
canvas = np.zeros((size+1, size+1, 3), dtype=np.uint8)
grey = np.asarray([70, 70, 70], dtype=np.uint8)
dgrey = np.asarray([35, 35, 35], dtype=np.uint8)
numi = 0
intersec = {}
colors = {1: np.asarray([200,50,50], dtype=np.uint8),
          2: np.asarray([75,75,200], dtype=np.uint8),
          3: np.asarray([50,200,50], dtype=np.uint8),
          4: np.asarray([10,50,200], dtype=np.uint8),
          5: np.asarray([10,50,250], dtype=np.uint8),
          6: np.asarray([50,50,50], dtype=np.uint8),
          7: np.asarray([100,50,50], dtype=np.uint8),
          8: np.asarray([0,255,0], dtype=np.uint8)}

def calc_manhattan(y, x):
    c_x = size//2
    c_y = size//2
    return int(abs(c_x-x) + abs(c_y-y))

def insert_pixel(y, x, color):
    canvas[y, x] = color

def check_pixel(x, y, c):
    if np.array_equal(canvas[x, y], black) or np.array_equal(canvas[x, y], grey) or np.array_equal(canvas[x, y], dgrey):
        return True
    elif np.array_equal(canvas[x, y], c):
        return True
    else:
        dists.append(calc_manhattan(x, y))
        numi += numi + 1 
        intersec[numi] = (y, x)
        return False

def write_intersection(y, x):
    insert_pixel(y, x, white)

def up(steps, pos, color):
    i = 0
    for i in range(0, steps+1):
        if check_pixel(pos[0]-i, pos[1], color):
            insert_pixel(pos[0]-i, pos[1], color)
        else:
            write_intersection(pos[0]-i, pos[1])
    r = [pos[0]-i, pos[1]]
    return r

def down(steps, pos, color):
    i = 0
    for i in range(0, steps+1):
        if check_pixel(pos[0]+i, pos[1], color):
            insert_pixel(pos[0]+i, pos[1], color)
        else:
            write_intersection(pos[0]+i, pos[1])            
    r = [pos[0]+i, pos[1]]
    return r

def left(steps, pos, color):
    i = 0
    for i in range(0, steps+1):
        if check_pixel(pos[0],pos[1]-i, color):
            insert_pixel(pos[0], pos[1]-i, color)
        else:
            write_intersection(pos[0]-i, pos[1])
    r = [pos[0], pos[1]-i]
    return r

def right(steps, pos, color):
    i = 0
    for i in range(0, steps+1):
        if check_pixel(pos[0],pos[1]+i, color):
            insert_pixel(pos[0], pos[1]+i, color)
        else:
            write_intersection(pos[0]-i, pos[1])
    r = [pos[0], pos[1]+i]
    return r

def draw_line(direction, steps, pos, color):
    if direction == 'U':
        pos = up(steps, pos, color)
    elif direction == 'D':
        pos = down(steps, pos, color)
    elif direction == 'L':
        pos = left(steps, pos, color)
    elif direction == 'R':
        pos = right(steps, pos, color)
    else:
        print("Unknown direction")
    return pos

def render_file(in_file, expected=None, img=None):
    with open(in_file) as f:
        line = f.readline()
        line_num = 1
        while line:
            l = line.split(',')
            pos = [size//2, size//2]
            for i in l:
                direction = i[0]
                steps = int(i[1:])
                pos = draw_line(direction, steps, pos, colors[line_num])
            print(colors[line_num])

            line_num += 1
            pos = [size//2, size//2]
            line = f.readline()
    canvas[size//2, size//2] = colors[8]
    numbers = list(filter(lambda num: num != 0, dists))
    numbers.sort()
    print("file: ", in_file, "result: ", min(numbers))
    print(intersec)
    del numbers
    if expected:
        print(expected)
    if img:
        Image.fromarray(canvas, mode='RGB').save(img)

def grey_checkers():
    for x in range(0, size, 2):
        for y in range(0, size, 2):
            canvas[y, x] = grey
            canvas[y+1, x+1] = grey


def main():
    #grey_checkers()
    """
    test_canvas = np.zeros((10, 10, 3), dtype=np.uint8)
    test_canvas[0, 0] = colors[8]
    Image.fromarray(test_canvas, mode="RGB").save('test_canv.png')
    """
    """
    canvas[3,1] = colors[8]
    render_file("test0", 6, 'test0.png')
    dists.clear()
    render_file("test1", 159, 'test1.png')
    dists.clear()
    render_file("test2", 135, 'test2.png')    
    """
    dists.clear()
    render_file("input")
    
if __name__ == '__main__':
    main()
