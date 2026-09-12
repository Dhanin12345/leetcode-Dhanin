# Last updated: 9/12/2026, 10:20:29 AM
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
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos = [0] * n
        for i, v in enumerate(nums2):
            pos[v] = i

        # Transform nums1 into positions in nums2
        arr = [pos[v] for v in nums1]

        fenwick1 = Fenwick(n)  # count of elements
        fenwick2 = Fenwick(n)  # count of pairs
        res = 0

        for x in arr:
            left_count = fenwick1.query(x - 1)   # how many before x
            pair_count = fenwick2.query(x - 1)   # how many pairs before x
            res += pair_count

            fenwick1.update(x, 1)                # add single element
            fenwick2.update(x, left_count)       # add pairs formed with x

        return res


# Example usage
if __name__ == "__main__":
    solver = Solution()
    print(solver.goodTriplets([2,0,1,3], [0,1,2,3]))   # Output: 1
    print(solver.goodTriplets([4,0,1,3,2], [4,1,0,2,3])) # Output: 4
