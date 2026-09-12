# Last updated: 9/12/2026, 10:19:48 AM
class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

        ans = 0
        for count in freq.values():
            if count == max_freq:
                ans += count

        return ans