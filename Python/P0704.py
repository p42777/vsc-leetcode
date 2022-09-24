from ast import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle # found target 
                
            elif nums[middle] < target:
                left = middle + 1 # search right

            else:
                right = middle - 1 # search left
       
        return -1 # target not found
