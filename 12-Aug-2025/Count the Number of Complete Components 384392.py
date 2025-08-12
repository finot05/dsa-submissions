# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[x] > self.rank[y]:
                self.parent[rooty] = rootx
            elif self.rank[x] < self.rank[y]:
                self.parent[rootx] = rooty
            else:
                self.parent[rootx] = rooty
                self.rank[y] += 1
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = DSU(n)
        for a, b in edges:
            uf.union(a, b)
        comps = defaultdict(list)
        for node in range(n):
            root = uf.find(node)
            comps[root].append(node)
        complete = 0
        for comp in comps.values():
            k = len(comp)
            m = 0
            cset = set(comp)
            for a, b in edges:
                if a in cset and b in cset:
                    m += 1
            if m == k*(k-1)/2:
                complete += 1
        return complete