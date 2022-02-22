
# Read the navigation data from the nav_file
def read_nav(nav_file):
    lines = open(nav_file).read().strip().splitlines()
    return lines

# Eliminate all closed chunks from the dataset
def process_data(data):    
    corrupt, incomplete = [], []
    
    for i, line in enumerate(data):
        # For each line, iteratively delete all correctly closed chunks
        while True:
            line_len = len(line)
            # Delete all correct chunks from the dataset
            for i in range(4):
                line = line.replace(openers[i]+closers[i], '')
            
            # If all of the correct chunks aren't removed, continue
            # Otherwise, separate the corrupted from the incomplete
            if line_len == len(line):
                break
        
        # Once the line is processed, determine whether it's corrupted or not 
        corrupted = False
        for closer in closers:
            if closer in line:
                corrupt.append(line)
                corrupted = True
                break # Move to next line if found to be corrupt
        if not corrupted:
            incomplete.append(line)
                
    return corrupt, incomplete


# Tally the corrupt closers
def quantify_corrupt(corrupt):
    illegal_closers = []
    for line in corrupt:
        for point in line:
            if point in closers:
                illegal_closers.append(point)
                break

    tally = 0
    for closer in illegal_closers:
        tally += chunk_points[closer]
    return tally

def tally_incomplete(incomplete):
    tallies = []
    for line in incomplete:
        tally = 0
        line = line[::-1]
        for char in line:
            tally *= 5
            tally += closer_points[closing_pair[char]]
        
        tallies.append(tally)
    
    tallies = sorted(tallies)
    
    return tallies[len(tallies) - len(tallies)//2 - 1]

def main(nav_file):
    # Retrieve the nav_data
    data = read_nav(nav_file)    
    corrupt, incomplete = process_data(data)
    
    corrupt_tally = quantify_corrupt(corrupt)
    print (f'Total syntax error: {corrupt_tally}')
    
    incomplete_tally = tally_incomplete(incomplete)
    print (f'Middle incomplete score: {incomplete_tally}')
    
    
    return


if __name__ == "__main__":
    nav_file = "Day 10.txt"
    openers = ['(', '{', '[', '<']
    closers = [')', '}', ']', '>']
    chunk_points = {')':3, ']':57, '}':1197, '>':25137}
    closer_points = {')':1, ']':2, '}':3, '>':4}
    closing_pair = {'(':')', '{':'}', '[':']', '<':'>'}
    
    main(nav_file)