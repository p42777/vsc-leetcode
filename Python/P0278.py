# The isBadVersion API is already defined
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # versions list already sorted
        min = 1
        max = n
        while min < max:
            middle = (min + max) // 2
            if isBadVersion(middle):
                max = middle
            else:
                min = middle + 1  # search right

        return max
