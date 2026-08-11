# Last updated: 8/11/2026, 4:02:46 PM
class Solution(object):
    def minElement(self, nums):
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        min_val = float('inf')
        
        for num in nums:
            min_val = min(min_val, digit_sum(num))
        
        return min_val
        