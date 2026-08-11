# Last updated: 8/11/2026, 4:02:42 PM
class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            t = (p + 1) & -(p + 1)
            ans.append(p - t // 2)
        
        return ans