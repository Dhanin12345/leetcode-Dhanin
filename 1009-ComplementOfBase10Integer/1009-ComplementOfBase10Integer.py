# Last updated: 9/12/2026, 10:23:27 AM
class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        
        mask = 1
        while mask <= n:
            mask <<= 1
        
        return (mask - 1) ^ n