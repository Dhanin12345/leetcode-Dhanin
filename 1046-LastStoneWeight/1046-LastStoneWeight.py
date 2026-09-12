# Last updated: 9/12/2026, 10:23:18 AM
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to max heap by storing negative values
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0   