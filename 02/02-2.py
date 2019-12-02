#!/usr/bin/env python3
from sys import exit

def get_input():
    f = open("input","r")
    return listify(f.read())


def listify(s):
    r = s.rstrip()
    l = r.split(',')    
    return list(map(int, l)) 

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

def run_program(l):
    for i in range(0, len(l), 4):
        wip, op = calc(wip, i)

def test_list(l, noun=None, verb=None):
    if noun != None:
        l[1] = noun
    if verb != None:
        l[2] = verb
    for i in range(0, len(l), 4):
        if l[i] == 99:
            break
        if l[i] not in (1, 2):
            break
        l, _ = calc(l, i)
    return l

def t1(s1, s2):
    s1 = listify(s1)
    r = test_list(s1)
    final = ','.join(map(str, r))
    if final == s2:
        print('true')
    else:
        print('false', r, "res: ", s2)

def main():
    ex1 = "1,0,0,0,99"
    ex2 = "2,3,0,3,99"
    ex3 = "2,4,4,5,99,0"
    ex4 = "1,1,1,4,99,5,6,0,99"

    res1 = "2,0,0,0,99"
    res2 = "2,3,0,6,99"
    res3 = "2,4,4,5,99,9801"
    res4 = "30,1,1,4,2,5,6,0,99"

    for test in ['ex1', 'ex2', 'ex3', 'ex4']:
        if test == 'ex1':
            t1(ex1, res1)
        elif test == 'ex2':
            t1(ex2, res2)
        elif test == 'ex3':
            t1(ex3, res3)
        elif test == 'ex4':        
            t1(ex4, res4)
    for i in range(0, 99):
        for j in range(0, 99):
            start_list = get_input()
            foo = test_list(start_list, i, j)
            if foo[0] == 19690720:
                r = 100 * i + j
                print(r)

if __name__ == '__main__':
    main()
