#!/usr/bin/env python3
import numpy as np

def main():
    f = open("input","r")
    content = f.read()
    w, h = np.meshgrid(np.arange(10), np.arange(10), sparse=False)
    data = []
    for i in w:
        for j in h:
            data[i][j] = '.'
    print(data)

if __name__ == '__main__':
    main()
