

file = '/Users/jacobbumgarner/Desktop/Advent of Code 2021/Day 0 C1.txt'

    
### Sliding Three measurement box
# 'Fancier' solution. 
def part2_oneline(depths, window=3):
    increased = sum(sum(depths[i:i+window]) < sum(depths[i+1:i+1+window]) 
                     for i in range(len(depths)-window+1))
    return increased

# First pass implementation.
def part2_first_pass(depths, window=3):
    increased = 0
    for i in range(len(depths)-window+1):
        increase = sum(depths[i+1:i+1+window]) > sum(depths[i:i+window])
        increased += increase
    return increased


### Previous measurement sums
# Found online, I like this zip method a lot!!
def part1(depths):
    # # My original
    # previous = depths[0]
    # increased = 0
    # for depth in depths:
    #     if depth > previous:
    #         increased += 1
    #     previous = depth
    increased = sum([previous < new for previous, new in zip(depths, depths[1:])])
    return increased


    
if __name__ == '__main__':
    with open(file, 'r') as f:
        depths = [int(depth) for depth in f]
    print (part2_first_pass(depths))
    print (part2_oneline(depths))


    
