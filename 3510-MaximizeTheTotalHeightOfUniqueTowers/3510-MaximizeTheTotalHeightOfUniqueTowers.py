# Last updated: 8/11/2026, 4:02:53 PM
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