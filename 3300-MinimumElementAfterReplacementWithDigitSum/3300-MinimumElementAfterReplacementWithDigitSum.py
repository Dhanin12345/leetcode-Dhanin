# Last updated: 9/12/2026, 10:19:11 AM
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
        