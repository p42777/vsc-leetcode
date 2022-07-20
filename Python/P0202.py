class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        for i in range(46340):
            if n in s: # cycle
                return False 
            s.add(n)

            n = sum([int(x) ** 2 for x in str(n)]) # sum of square of digits
            if n == 1:
                return True
        return True
