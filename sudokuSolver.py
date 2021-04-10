
rows = []
cols = []
blocks = []

def convert(i, j):
     return (i // 3) * 3 + j // 3

def check_if_correct(board, i, j, val):
    block_id = convert(i, j)
    return not (val in rows[i] or val in cols[j] or val in blocks[block_id])
    
class Solution(object):
    def __init__(self):
        self.solved = False
        
    def soduku_helper(self, board, positions, index):
        if index == len(positions):
            return True

        i, j = positions[index]
        for val in range(1,10):
            if check_if_correct(board, i, j, val): 
                rows[i].add(val)
                cols[j].add(val)
                blocks[convert(i,j)].add(val)

                board[i][j] = str(val)

                if not self.soduku_helper(board, positions, index+1):
                    board[i][j] = '.'
                    rows[i].remove(val)
                    cols[j].remove(val)
                    blocks[convert(i,j)].remove(val)
                else:
                    return True
        return False


    def solveSudoku(self, board):
        global rows, cols, blocks
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col]!='.':
                    rows[row].add(int(board[row][col]))
                    cols[col].add(int(board[row][col]))
                    blocks[convert(row, col)].add(int(board[row][col]))
         
        positions = [(row, col) for row in range(9) for col in range(9) if board[row][col]=='.']
        # helper - use for backtracking
        self.soduku_helper(board, positions, 0)
            
      

  
