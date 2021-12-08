
import numpy as np
from time import perf_counter as pf

def read_positions(file):
    subs = np.array(open(file).read().split(','), dtype=int)
    return subs

def sub_convergence(subs, increasing_cost=False):
    t = pf()
    stdev = np.std(subs)
    upper, lower = int(np.mean(subs)+ stdev), max(0, int(np.mean(subs) - stdev))
    min_fuel = 10**10
    for position in range(lower, upper+1):
        # print (f'{position}/{upper} positions tested...')
        if increasing_cost:
            candidate_fuel = 0
            cost = 1
            test_sub = subs.copy()
            while np.any(test_sub != position):
                candidate_fuel += np.count_nonzero(test_sub != position) * cost
                test_sub[test_sub < position] += 1
                test_sub[test_sub > position] -= 1
                cost += 1
        else:
            candidate_fuel = np.abs(subs - position).sum()
        if candidate_fuel < min_fuel:
            min_fuel = candidate_fuel
    print ("Optimal position identified!")
    print (pf() - t)
    return min_fuel

if __name__ == '__main__':
    file = 'Day 7.txt'
    subs = read_positions(file)
    print (sub_convergence(subs, increasing_cost=True))