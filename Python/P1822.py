from ast import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        if 0 in nums:
            return 0
        else:
            for x in nums:
                product *= x
        if product < 0:
            return -1
        else:
            return 1
