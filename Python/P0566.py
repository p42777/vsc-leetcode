from ast import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        M = len(mat)
        N = len(mat[0])
        if (M * N != r * c): return mat; # return original if no match

        res = [[0 for _ in range(c)] for _ in range(r)]
        temp = []
        k = 0

        # flatten the list
        for i in range(M):
            for j in range(N):
                temp.append(mat[i][j])

        for i in range(r):
            for j in range(c):
                res[i][j] = temp[k]
                k += 1

        return res
    
