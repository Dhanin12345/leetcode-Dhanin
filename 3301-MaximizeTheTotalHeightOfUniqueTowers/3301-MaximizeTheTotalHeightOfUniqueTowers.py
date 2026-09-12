# Last updated: 9/12/2026, 10:19:21 AM
class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        maximumHeight.sort(reverse=True)
        
        total = 0
        prev = float('inf')
        
        for h in maximumHeight:
            curr = min(h, prev - 1)
            
            if curr <= 0:
                return -1
            
            total += curr
            prev = curr
        
        return total