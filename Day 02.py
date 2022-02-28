

import numpy as np
file = '/Users/jacobbumgarner/Desktop/Advent of Code 2021/Day 1.txt'

# Set up our directions array
def decode_directions(movements):
    indices = [None, 'f', 'd', 'u'] # Keeping consistent with instructions
    directions = np.array([indices.index(mvmt[0]) for mvmt in movements])
    mvmts = np.array([int(mvmt[-1]) for mvmt in movements])
    return directions, mvmts

def part1(movements):
    directions, mvmts = decode_directions(movements)
    X = np.sum(mvmts[directions==1])
    Y = np.sum(mvmts[directions==2]) - np.sum(mvmts[directions==3])
    return X*Y

def part2(movements):
    directions, mvmts = decode_directions(movements)
    aim = X = Y = 0
    for d, m in zip(directions, mvmts):
        if d == 1:
            X += m
            Y += aim*m
        elif d == 2 or d == 3:
            aim += m if d == 2 else -m
    return  X*Y
    
if __name__ == '__main__':
    with open(file, 'r') as f:
        movements = [mvmt.strip('\n') for mvmt in f]
    print(part1(movements))
    print (part2(movements))
