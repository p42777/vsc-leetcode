from ast import List

class Solution:
    def twoSum(self, nums : List[int], target : int) -> List[int]:
        hashMap = {} # HashMap for previous index and values

        # iterate through array elements
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[n] = i

        return
