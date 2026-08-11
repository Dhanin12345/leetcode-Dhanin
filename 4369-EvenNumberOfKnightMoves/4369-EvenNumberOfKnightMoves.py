# Last updated: 8/11/2026, 4:02:11 PM
class Solution(object):
    def canReach(self,start,target):
        return(start[0] + start[1]) %2 == (target[0] + target[1]) %2