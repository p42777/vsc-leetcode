import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        counter = collections.Counter(s)

        for i in range(len(s)):
            if counter.get(s[i]) == 1:
                return i
        
        return -1
