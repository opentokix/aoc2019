#!/usr/bin/env python3

def div_fuel(d):
    return d//3-2

def calc_fuel_for_module(d):
    cutoff = 8
    rest = d
    stack = 0
    while rest > cutoff:
        rest = div_fuel(rest)
        stack = stack + rest
    return stack

def main():
    r = []
    with open("input") as f:
        for line in f:
            s = int(line.rstrip())
            r.append(calc_fuel_for_module(s))

    print(sum(r))
if __name__ == '__main__':
    main()
