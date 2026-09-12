# Last updated: 9/12/2026, 10:21:28 AM
class Solution:

    def minDays(self, grid):
        m, n = len(grid), len(grid[0])

        def count_islands():
            visited = [[False] * n for _ in range(m)]

            def dfs(x, y):
                stack = [(x, y)]
                visited[x][y] = True

                while stack:
                    i, j = stack.pop()
                    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            if grid[ni][nj] == 1 and not visited[ni][nj]:
                                visited[ni][nj] = True
                                stack.append((ni, nj))

            islands = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)

            return islands

        # Step 1: already disconnected
        if count_islands() != 1:
            return 0

        # Step 2: try removing one cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        # Step 3
        return 2