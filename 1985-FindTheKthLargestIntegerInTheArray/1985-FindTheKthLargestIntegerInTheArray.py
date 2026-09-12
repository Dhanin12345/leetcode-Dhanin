# Last updated: 9/12/2026, 10:20:41 AM
import heapq

class Solution:
    def kthLargestNumber(self, nums, k):

        def key(x):
            return (int(x), x)  # safe but slower

        heap = []

        for x in nums:
            heapq.heappush(heap, int(x))

        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return str(heap[0])