# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(n * n * 4)
        
        for i in range(n):
            for j in range(n):
                idx = (i * n + j) * 4
                val = grid[i][j]
                
                if val == ' ':
                    dsu.union(idx + 0, idx + 1)
                    dsu.union(idx + 1, idx + 2)
                    dsu.union(idx + 2, idx + 3)
                elif val == '/':
                    dsu.union(idx + 0, idx + 3)
                    dsu.union(idx + 1, idx + 2)
                elif val == '\\':
                    dsu.union(idx + 0, idx + 1)
                    dsu.union(idx + 2, idx + 3)
                    
                if j + 1 < n:
                    r_idx = (i * n + (j + 1)) * 4
                    dsu.union(idx + 1, r_idx + 3)
                    
                if i + 1 < n:
                    b_idx = ((i + 1) * n + j) * 4
                    dsu.union(idx + 2, b_idx + 0)

        regions = sum(dsu.find(x) == x for x in range(n * n * 4))
        return regions


        