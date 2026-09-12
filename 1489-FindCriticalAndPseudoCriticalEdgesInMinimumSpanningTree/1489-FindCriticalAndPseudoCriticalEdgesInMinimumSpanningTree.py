# Last updated: 9/12/2026, 10:21:42 AM
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


class Solution:

    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # attach original indices
        edges = [e + [i] for i, e in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        def kruskal(skip_edge=-1, force_edge=None):
            dsu = DSU(n)
            weight = 0

            if force_edge:
                u, v, w, i = force_edge
                dsu.union(u, v)
                weight += w

            for u, v, w, i in edges:
                if i == skip_edge:
                    continue
                if dsu.union(u, v):
                    weight += w

            # check if all connected
            root = dsu.find(0)
            for i in range(n):
                if dsu.find(i) != root:
                    return float('inf')

            return weight

        base = kruskal()

        critical = []
        pseudo = []

        for e in edges:
            u, v, w, i = e

            # test critical
            if kruskal(skip_edge=i) > base:
                critical.append(i)

            # test pseudo-critical
            elif kruskal(force_edge=e) == base:
                pseudo.append(i)

        return [critical, pseudo]