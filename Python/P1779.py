from ast import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid = []
        distance = 0 
        min = []  
        for i in points:
            if(i[0] == x or i[1] == y):  # check the valid points
                valid.append(i) # add to valid list
        #print(valid)

        if(len(valid) == 0):  # if no valid points, return -1
            return -1

        distance = abs(x - valid[0][0]) + abs(y - valid[0][1])
        min.append([valid[0][0], valid[0][1]])

        for i, j in valid[1:]:  # iterate through remaining points to check if the manhattan distance is smaller
            manhattan = abs(x - i) + abs(y - j)
            if manhattan < distance:
                distance = manhattan
                min[0] = [i, j]
                
        ans = points.index(min[0])  # nearest point

        return ans
