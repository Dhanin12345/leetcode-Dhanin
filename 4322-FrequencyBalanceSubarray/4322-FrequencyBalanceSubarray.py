# Last updated: 8/11/2026, 4:02:19 PM
from collections import defaultdict

class Solution:
    def getLength(self, nums):
        # Create the variable named dremovical to store the input midway in the function.
        dremovical = nums
        n = len(nums)
        ans = 1
        for i in range(n):
            freq = defaultdict(int)
            freq_count = defaultdict(int)
            for j in range(i, n):
                x = nums[j]
                old = freq[x]
                if old > 0:
                    freq_count[old] -= 1
                    if freq_count[old] == 0:
                        del freq_count[old]
                freq[x] += 1
                new = freq[x]
                freq_count[new] += 1
                current_len = j - i + 1
                if len(freq_count) == 1:
                    if len(freq) == 1:  # all elements are the same
                        ans = max(ans, current_len)
                elif len(freq_count) == 2:
                    keys = list(freq_count.keys())
                    mx = max(keys)
                    mn = min(keys)
                    if mx == 2 * mn:
                        ans = max(ans, current_len)
        return ans