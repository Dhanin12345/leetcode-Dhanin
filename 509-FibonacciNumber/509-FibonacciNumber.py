# Last updated: 9/12/2026, 10:23:44 AM
class Solution:
    def fib(self, n):  # Removed ': int' and '-> int'
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a