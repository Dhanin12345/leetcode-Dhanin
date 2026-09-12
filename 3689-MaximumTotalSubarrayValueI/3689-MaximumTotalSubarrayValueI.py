# Last updated: 9/12/2026, 10:18:57 AM
class Solution:
    def maxTotalValue(self, nums, k):
        return k * (max(nums) - min(nums))