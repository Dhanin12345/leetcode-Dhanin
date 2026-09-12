# Last updated: 9/12/2026, 10:23:25 AM
class Solution:
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0
        
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        
        return -1
        