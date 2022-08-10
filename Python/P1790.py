class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        map1, map2 = {}, {}

        for i in s1:
            map1[i] = map1.get(i, 0) + 1

        for i in s2:
            map2[i] = map2.get(i, 0) + 1

        if map1 != map2:
            return False
        else:
            diff = 0
            for i, j in zip(s1, s2): # join two tuples
                if i != j:
                    diff += 1

        # only one string swap (difference = 2)
        return diff == 2
