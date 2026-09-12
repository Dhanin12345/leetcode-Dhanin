# Last updated: 9/12/2026, 10:21:06 AM
class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for i in range(m):
            # Step 1: Update heights
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Step 2: Sort heights in descending order
            sorted_heights = sorted(heights, reverse=True)
            
            # Step 3: Calculate max area
            for j in range(n):
                area = sorted_heights[j] * (j + 1)
                max_area = max(max_area, area)
        
        return max_area
        