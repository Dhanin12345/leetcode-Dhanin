# Last updated: 8/11/2026, 4:03:16 PM
class Solution:
    def missingInteger(self, nums):
        total = nums[0]
        i = 1

        # Find longest sequential prefix
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Store all numbers
        seen = set(nums)

        # Find missing number >= total
        while total in seen:
            total += 1

        return total