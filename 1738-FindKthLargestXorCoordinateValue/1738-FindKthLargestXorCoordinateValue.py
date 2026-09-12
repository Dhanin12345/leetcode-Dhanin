# Last updated: 9/12/2026, 10:21:03 AM
class Solution:
    def kthLargestValue(self, matrix, k):

        m, n = len(matrix), len(matrix[0])
        px = [[0] * n for _ in range(m)]
        values = []

        for i in range(m):
            for j in range(n):
                val = matrix[i][j]

                if i > 0:
                    val ^= px[i - 1][j]
                if j > 0:
                    val ^= px[i][j - 1]
                if i > 0 and j > 0:
                    val ^= px[i - 1][j - 1]

                px[i][j] = val
                values.append(val)

        values.sort(reverse=True)
        return values[k - 1]