import numpy as np

# Read the text file
def load_grid(grid_file):
    raw = open(grid_file).read().strip().splitlines()
    raw_grid = [[int(octopus) for octopus in line] for line in raw]
    grid = np.array(raw_grid, dtype=np.int_)
    return np.pad(grid, 1)

# Flash the space surrounding the point, set point to low value
def flash(grid, point, pad_reset):
    x, y = point
    grid[x-1:x+2, y-1:y+2] += 1
    grid *= pad_reset
    grid[x,y] = -10000
    return grid

# Count the number of flashes, or the synchronized step
def count_flashes(grid, iterations=100):
    flash_count = 0
    pad_reset = np.zeros(grid.shape, dtype=np.int_)
    pad_reset[1:-1, 1:-1] += 1
    
    synchronized_step = 0
    
    i = 0
    # for i in range(iterations):
    while True:
        grid += 1
        
        while True:
            flashes = np.argwhere(grid > 9)
            if not np.any(flashes):
                break   
            grid = flash(grid, flashes[0], pad_reset)
            flash_count += 1
        
        grid[grid > 9] = 0
        grid[grid < 0] = 0
        grid *= pad_reset
        
        if np.sum(grid) == 0:
            synchronized_step = i+1
            break
        
        i += 1
    
    return flash_count, synchronized_step

def main(grid_file):
    grid = load_grid(grid_file)
    
    flash_count, synchronized_step = count_flashes(grid, iterations=100)
    print (f"Flashes: {flash_count}, Synchrony Step: {synchronized_step}")
    return


if __name__ == "__main__":
    grid_file = "Day 11.txt"
    main(grid_file)