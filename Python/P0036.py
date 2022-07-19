from ast import List
import collections

class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 HashSets
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        sub_square = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                sub_r = r // 3
                sub_c = c // 3

                if board[r][c] == '.' : continue
                if(board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sub_square[sub_r, sub_c]):
                    # duplicate
                    return False

                # add to three HashSets and keep checking if no duplicate
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                sub_square[sub_r, sub_c].add(board[r][c])

        return True





