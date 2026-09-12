# Last updated: 9/12/2026, 10:21:23 AM
class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        # Precompute combinations
        n = len(nums)
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

        # Build BST implicitly using recursion
        def dfs(arr):
            if len(arr) <= 2:
                return 1, len(arr)

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left_ways, left_size = dfs(left)
            right_ways, right_size = dfs(right)

            total_ways = comb[left_size + right_size][left_size]
            total_ways = (total_ways * left_ways * right_ways) % MOD

            return total_ways, left_size + right_size + 1

        return (dfs(nums)[0] - 1) % MOD