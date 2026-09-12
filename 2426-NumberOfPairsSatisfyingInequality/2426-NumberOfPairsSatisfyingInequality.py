# Last updated: 9/12/2026, 10:20:23 AM
from bisect import bisect_right

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res


class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        arr = [nums1[i] - nums2[i] for i in range(n)]

        # Coordinate compression
        values = sorted(set(arr + [x + diff for x in arr]))
        fenwick = Fenwick(len(values))

        res = 0
        for x in arr:
            # Count how many arr[i] <= x + diff
            idx = bisect_right(values, x + diff) - 1
            res += fenwick.query(idx)

            # Insert current arr[j]
            fenwick.update(bisect_right(values, x) - 1, 1)

        return res


# 🔎 Example runs
solver = Solution()
print(solver.numberOfPairs([3,2,5], [2,2,1], 1))   # Output: 3
print(solver.numberOfPairs([3,-1], [-2,2], -1))    # Output: 0
