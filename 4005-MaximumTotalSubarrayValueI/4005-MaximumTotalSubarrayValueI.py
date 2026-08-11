# Last updated: 8/11/2026, 4:02:33 PM
class Solution:
    def maxTotalValue(self, nums, k):
        return k * (max(nums) - min(nums))