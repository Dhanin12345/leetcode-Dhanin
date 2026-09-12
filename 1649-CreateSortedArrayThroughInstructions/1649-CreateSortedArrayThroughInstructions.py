# Last updated: 9/12/2026, 10:21:13 AM
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        max_val = max(instructions)

        bit = Fenwick(max_val)

        cost = 0

        for i, x in enumerate(instructions):
            less = bit.query(x - 1)          # count < x
            total = i                        # already inserted elements
            greater = total - bit.query(x)   # count > x

            cost = (cost + min(less, greater)) % MOD

            bit.update(x, 1)

        return cost