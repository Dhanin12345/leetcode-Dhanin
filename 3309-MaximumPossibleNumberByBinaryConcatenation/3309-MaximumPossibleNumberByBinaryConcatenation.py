# Last updated: 9/12/2026, 10:19:18 AM
class Solution(object):
    def maxGoodNumber(self, nums):
        from itertools import permutations
        
        # Convert to binary strings
        binaries = [bin(x)[2:] for x in nums]
        
        max_val = 0
        
        # Try all permutations
        for perm in permutations(binaries):
            combined = ''.join(perm)
            max_val = max(max_val, int(combined, 2))
        
        return max_val