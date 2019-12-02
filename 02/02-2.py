#!/usr/bin/env python3
from sys import exit

def get_input():
    f = open("input","r")
    content = f.read()
    content = content.rstrip()
    l = content.split(',')
    wip = list(map(int, l))
    return wip


def calc(l, pos):
    if l[pos] == 2:
       store_pos = l[pos+3]
       val1 = l[l[pos+1]]
       val2 = l[l[pos+2]]
       l[store_pos] = val1 * val2 
       return l, l[pos]
    elif l[pos] == 1:
       store_pos = l[pos+3]
       val1 = l[l[pos+1]]
       val2 = l[l[pos+2]]
       l[store_pos] = val1 + val2 
       return l, l[pos]
    elif l[pos] == 99:
        return l, l[pos]
    else: 
        print("unknown op code", l[pos])
        return l, l[pos]

def run_program(l):
    for i in range(0, len(l), 4):
        wip, op = calc(wip, i)
    if op == '99':
        return wip[0]
    else: 
        print ("error: ", wip[0])
        return 1

def main():
    initial = get_input()
    num_runs = 0 
    for noun in range(0, 99):
        for verb in range(0, 99):
            num_runs += 1 
            wip = initial  
            wip[1] = noun
            wip[2] = verb
            print(num_runs)
            for i in range(0, len(wip), 4):
                wip = calc(wip, i)
                if wip[0] == "19690720":
                    result = 100 * noun + verb 
                    print(result)
                    exit(0)
    

if __name__ == '__main__':
    main()
