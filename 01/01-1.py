#!/usr/bin/env python3

def div_fuel(d):
    return d//3-2

def main():
    r = []
    with open("input") as f:
        for line in f:
            s = line.rstrip()
            d = div_fuel(int(s))
            r.append(d)

    print(sum(r))
if __name__ == '__main__':
    main()
