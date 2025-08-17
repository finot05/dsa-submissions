# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

n, m = map(int, input().split())
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rootx] = rooty
            return True
        return False
dsu = DSU(n)
mst_weight = 0
edges = []
edges_used = 0
for i in range(m):
    b, e, w = map(int, input().split())
    edges.append((w, b, e))
edges.sort()
for w, b, e in edges:
    if dsu.union(b, e):
        mst_weight += w
        edges_used += 1
        if edges_used == n - 1:
            break
print(mst_weight)
