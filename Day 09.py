
import numpy as np
from scipy.ndimage import label

def read_map(file):
    map = np.array([[num for num in line] for line in open(file).read().strip().splitlines()],
                   dtype=int)
    map = np.pad(map, 1, constant_values=9)
    return map

def find_minima(map, filter):
    min_row = []
    min_col = []
    for i in range(1, map.shape[0]-1):
        for j in range(1, map.shape[1]-1):
            if np.all(map[i-1:i+2, j-1:j+2]+filter > map[i, j]):
                min_row.append(i)
                min_col.append(j)
    part1 = np.sum(map[min_row, min_col])+len(min_row)
    map[map==9] = -1
    map = (map > -1).astype(int)
    labeled, basins = label(map, structure=np.array([[0,1,0],[1,1,1],[0,1,0]]))
    sizes = np.array([np.count_nonzero(labeled == label) for label in range(1, basins+1)])
    part2 = np.prod(np.sort(sizes)[-3:])
    return part1, part2

if __name__ == "__main__":
    filter = np.array([[10,0,10],
                       [0,10,0],
                       [10,0,10]])
    file = 'Day 9.txt'
    map = read_map(file)
    print (find_minima(map, filter))
