class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        n = str(n)
        for element in n:
            sum = sum + int(element)
            product = product * int(element)
        return product - sum
        
