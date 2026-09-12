# Last updated: 9/12/2026, 10:23:58 AM
class Solution:
    def maxSubarraySumCircular(self, nums):

        total_sum = 0

        max_sum = float('-inf')
        cur_max = 0

        min_sum = float('inf')
        cur_min = 0

        for x in nums:
            total_sum += x

            # Kadane for max subarray
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

            # Kadane for min subarray
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

        # if all numbers are negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)