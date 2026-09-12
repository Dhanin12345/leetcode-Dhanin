# Last updated: 9/12/2026, 10:18:37 AM
class Solution(object):
    def canReach(self,start,target):
        return(start[0] + start[1]) %2 == (target[0] + target[1]) %2