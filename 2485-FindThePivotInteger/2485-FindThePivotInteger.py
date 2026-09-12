# Last updated: 9/12/2026, 10:20:15 AM
import math

class Solution:
    def pivotInteger(self, n):
        target = n * (n + 1) // 2
        x = int(math.sqrt(target))
        
        if x * x == target:
            return x
        return -1