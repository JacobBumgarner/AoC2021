
import numpy as np

def read_ages(file):
    ages = np.array(open(file).read().split(','), dtype=int)
    fish = np.histogram(ages, 10, range = (0, 10))[0]
    return fish

def part1(fish, days=80):
    for day in range(days):
        print (f"Day: {day}, bytes: {fish.nbytes}")
        fish -= 1
        new_fish = np.count_nonzero(fish == -1)
        fish[fish == -1] = 6
        fish = np.append(fish, np.full(new_fish, 8))
    return fish.shape[0]

# Histogram solution initially inspired by @adeak's solution
def fish_spawning(fish, days=80):
    for _ in range(days):
        spawners = fish[0]
        fish[:9] = fish[1:]
        fish[[6, 8]] += spawners
    return np.sum(fish)

if __name__ == "__main__":
    file = 'Day 6.txt'
    fish = read_ages(file)
    print (fish_spawning(fish, 256))
    
