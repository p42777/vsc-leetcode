from ast import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       ROWS = len(matrix)
       COLS = len(matrix[0])
       top = 0
       bot = ROWS - 1
       # First Binary Search to determine which row the value could be in
       while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
        if not top <= bot: return False
        row = (top + bot) // 2
        l = 0
        r = COLS - 1
        # Second Binary Search for current / the specified row
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else: 
                return True
        return False

