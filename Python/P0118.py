from ast import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            tmp = [0] + result[-1] + [0] # add zeros before & after the list
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(tmp[j] + tmp[j+1])
            result.append(row)

        return result
        


