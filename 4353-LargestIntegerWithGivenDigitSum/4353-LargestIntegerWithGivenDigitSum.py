# Last updated: 8/11/2026, 4:02:05 PM
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