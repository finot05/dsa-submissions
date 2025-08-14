# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # Path halving
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        return True

class Solution:
    def minCostConnectPoints(self, pts):
        n = len(pts)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(pts[i][0] - pts[j][0]) + abs(pts[i][1] - pts[j][1])
                edges.append((dist, i, j))

        edges.sort()

        dsu = DSU(n)
        mst_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            if dsu.union(u, v):
                mst_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break

        return mst_cost
