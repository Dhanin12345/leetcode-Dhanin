# Last updated: 9/12/2026, 10:18:39 AM
class Solution(object):
    def largestInteger(self, n, s):
        # Maximum possible sum using n digits is 9 * n
        if s > 9 * n:
            return -1
        
        digits = []
        
        for _ in range(n):
            d = min(9, s)
            digits.append(str(d))
            s -= d
            
        return int("".join(digits))