

import numpy as np
from numpy.lib.npyio import _loadtxt_dispatcher

file = 'Day 4.txt'

class Board:
    def __init__(self, board:np.ndarray, size=5):
        self.board = board
        self.board_cover = board.copy()
        self.row_hits = np.zeros(size)
        self.column_hits = np.zeros(size)
        self.won = False
        
def read_info(file, size=5):
    with open(file, 'r') as f:
        # Get the numbers
        info = f.read().split()
        numbers = [int(i) for i in info.pop(0).split(',')]
        # Get the boards
        boards = []
        for depth in range(int(len(info) / 25)):
            board_numbers = np.array([int(tile) for tile in info[depth*25:depth*25+25]]).reshape(5,5)
            boards.append(Board(board_numbers))
    return numbers, boards

def bingo(boards, numbers, last_winner=False):
    wins = 0
    for number in numbers:
        for board in boards:
            if board.won: # Don't play for solved boards
                continue
            
            hits = np.where(board.board == number)
            if len(hits[0]): # Add hits to rows and columns
                board.row_hits[hits[0]] += 1
                board.column_hits[hits[1]] += 1
                board.board[hits[0], hits[1]] = -1 # 'Cover' hit squares
                
            if np.any(board.row_hits == 5) or np.any(board.column_hits == 5):
                wins += 1 # Add to the tally if there is a winner
                board.won = True if wins < len(boards) - 1 else False # Mark the board as won (unless last winner)
                if not last_winner: # Return for part1
                    unhit = board.board[np.where(board.board != -1)]
                    return np.sum(board.board[np.where(board.board != -1)])*number
        
        if wins == len(boards) - 1: # Return for part 2 after finding last winner
            loser = [check for check in boards if not check.won][0]
            return np.sum(loser.board[np.where(loser.board != -1)])*number
    return


if __name__ == "__main__":
    numbers, boards = read_info(file)
    print (bingo(boards, numbers))
    print (bingo(boards, numbers, last_winner=True))