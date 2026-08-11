# Last updated: 8/11/2026, 4:03:12 PM
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