# Last updated: 9/12/2026, 10:23:41 AM
import heapq

class Solution:
    def kClosest(self, points, k):

        heap = []

        for x, y in points:
            dist = -(x*x + y*y)  # negative for max heap

            heapq.heappush(heap, (dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for (_, x, y) in heap]