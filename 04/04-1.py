#!/usr/bin/env python3

def check_password(password):
    wip = [int(i) for i in str(password)]
    flags = {'inc':     None, 
             'same':    None, 
             'six':     None, 
             'range':   None}
    for i in range(1, len(wip)):
        if wip[i] < wip[i-1]:
            flags['inc'] = False
            break
        else:
            flags['inc'] = True

    for i in range(1, len(wip)):
        if wip[i] == wip[i-1]:
            flags['same'] = True
            break
        else:
            flags['same'] = False
    return flags


def main():
    num_match = 0 
    f = open("input","r")
    content = f.read()
    content = content.rstrip()
    r = content.split('-')
    for i in range(int(r[0]), int(r[1])):
        result = check_password(i)
        if result['inc'] and result['same']:
            num_match += 1
    print("number of matches: ",num_match)
if __name__ == '__main__':
    main()
