#!/usr/bin/env python3
from sys import exit


def calc(l, pos):
    print(pos)
    if l[pos] == 2:
       store_pos = l[pos+3]
       val1 = l[l[pos+1]]
       val2 = l[l[pos+2]]
       print(val1, val2)
       l[store_pos] = val1 * val2 
       return l 
    elif l[pos] == 1:
       store_pos = l[pos+3]
       val1 = l[l[pos+1]]
       val2 = l[l[pos+2]]
       l[store_pos] = val1 + val2 
       return l 
    elif l[pos] == 99:
        print("Finished!")
        print(l)
        exit(0)
    else: 
        print("unknown op code")
        exit(1)

def main():
    f = open("input","r")
    content = f.read()
    content = content.rstrip()
    #content = "1,1,1,4,99,5,6,0,99"
    #content = "2,4,4,5,99,0"
    l = content.split(',')
    wip = list(map(int, l))
    for i in range(0,len(wip),4):
        wip = calc(wip, i)

if __name__ == '__main__':
    main()
