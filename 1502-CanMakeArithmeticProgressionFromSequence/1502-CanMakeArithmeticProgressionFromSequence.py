# Last updated: 9/12/2026, 10:21:35 AM
class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True