
import numpy as np

def read_diagnostics(file):
    with open(file, 'r') as f:
        raw = [info.strip() for info in f]
        diagnostics = np.zeros([len(raw), len(raw[0])], dtype=np.int8)
        for i, line in enumerate(raw):
            for j in range(diagnostics.shape[1]):
                diagnostics[i, j] = int(line[j])
    return diagnostics

def binary_to_int(array):
    integer = 0
    for i, number in enumerate(np.flip(array)):
        integer += number * 2**i
    return integer

def get_power_rating(diagnostics, zeros=False):
    binary = np.zeros(diagnostics.shape[1], dtype=np.int8)
    for i in range(diagnostics.shape[1]):
        ones = np.sum(diagnostics[:, i])
        if zeros:
            if ones < diagnostics.shape[0]/2:
                binary[i] = 1
        else:
            if ones >= diagnostics.shape[0]/2:
                binary[i] = 1
    return binary

def identify_LSR_component(diagnostics, epsilon=False):
    component_rating = diagnostics
    for i in range(component_rating.shape[1]):
        if component_rating.shape[0] == 1:
            break
        rating = get_power_rating(component_rating, zeros=epsilon)
        component_rating = component_rating[np.where(component_rating[:, i]==rating[i])[0]]
    return component_rating[0]

def part1(diagnostics):
    gamma = binary_to_int(get_power_rating(diagnostics))
    epsilon = binary_to_int(get_power_rating(diagnostics, zeros=True))    
    return int(gamma * epsilon)

def part2(diagnostics):
    oxygen_rating = binary_to_int(identify_LSR_component(diagnostics))
    scrubbing_rating = binary_to_int(identify_LSR_component(diagnostics, epsilon=True))
    return int(oxygen_rating*scrubbing_rating)


if __name__ == "__main__":
    file = '/Users/jacobbumgarner/Desktop/Advent of Code 2021/Day 2.txt'
    diagnostics = read_diagnostics(file)
    power_consumption = part1(diagnostics)
    LSR = part2(diagnostics)
    
    print (power_consumption)
    print (LSR)
