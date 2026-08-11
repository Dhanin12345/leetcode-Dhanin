# Last updated: 8/11/2026, 4:02:50 PM
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