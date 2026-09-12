# Last updated: 9/12/2026, 10:23:52 AM
class Solution:
    def beautifulArray(self, n):

        def build(arr):
            if len(arr) <= 1:
                return arr

            odds = build(arr[::2])   # index pattern
            evens = build(arr[1::2])

            return odds + evens

        return build(list(range(1, n + 1)))