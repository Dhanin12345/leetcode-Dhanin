# Last updated: 9/12/2026, 10:22:49 AM
class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c