# Last updated: 9/12/2026, 10:22:31 AM
from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery = [-1] * n
        low = [-1] * n
        time = [0]   # mutable container to avoid nonlocal issues
        bridges = []

        def dfs(node, parent):
            discovery[node] = low[node] = time[0]
            time[0] += 1

            for nei in graph[node]:
                if nei == parent:
                    continue

                if discovery[nei] == -1:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])

                    if low[nei] > discovery[node]:
                        bridges.append([node, nei])
                else:
                    low[node] = min(low[node], discovery[nei])

        dfs(0, -1)
        return bridges