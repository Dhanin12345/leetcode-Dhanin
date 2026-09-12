# Last updated: 9/12/2026, 10:20:18 AM
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, idx, val, node, l, r):
        if l == r:
            self.tree[node] = max(self.tree[node], val)
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(idx, val, 2*node, l, mid)
        else:
            self.update(idx, val, 2*node+1, mid+1, r)
        self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])

    def query(self, ql, qr, node, l, r):
        if qr < l or ql > r:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return max(self.query(ql, qr, 2*node, l, mid),
                   self.query(ql, qr, 2*node+1, mid+1, r))


class Solution:
    def lengthOfLIS(self, nums, k):
        max_val = max(nums)
        seg = SegmentTree(max_val)
        res = 0

        for x in nums:
            # Query best dp in range [x-k, x-1]
            left = max(1, x - k)
            right = x - 1
            best = seg.query(left, right, 1, 1, max_val) if right >= left else 0
            dp = best + 1
            seg.update(x, dp, 1, 1, max_val)
            res = max(res, dp)

        return res


# 🔎 Example runs
solver = Solution()
print(solver.lengthOfLIS([4,2,1,4,3,4,5,8,15], 3))  # Output: 5
print(solver.lengthOfLIS([7,4,5,1,8,12,4,7], 5))    # Output: 4
print(solver.lengthOfLIS([1,5], 1))                 # Output: 1
