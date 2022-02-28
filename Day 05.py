import numpy as np

file = 'Day 5.txt'

def read_file(file):
    info = open(file).read().strip().splitlines()
    starts = np.zeros([len(info), 2], dtype=np.int_)
    ends = np.zeros([len(info), 2], dtype=np.int_)
    for i, coords in enumerate(info):
        coords = coords.split(' -> ')
        starts[i] = coords[0].split(',')
        ends[i] = coords[1].split(',')
    return starts, ends, max(np.max(starts), np.max(ends))+1

def mapper(starts, ends, size, diagonals=False):
    map = np.zeros([size, size])
    for s,e in zip(starts, ends):
        if diagonals or s[0]==e[0] or s[1]==e[1]:
            points = np.max(np.abs(s-e))+1
            xs = np.linspace(s[0], e[0], points, dtype=int)
            ys = np.linspace(s[1], e[1], points, dtype=int)
            map[[ys], [xs]] += 1
    return np.count_nonzero(map > 1)


if __name__ == "__main__":
    starts, ends, size = read_file(file)
    print (mapper(starts, ends, size))
    print (mapper(starts, ends, size, diagonals=True))
