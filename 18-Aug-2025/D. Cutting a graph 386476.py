# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

n, m, k = map(int, input().split())

edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

oprs = []
for _ in range(k):
    line = input().split()
    opr, u, v = line[0], int(line[1]), int(line[2])
    oprs.append((opr, u, v))

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

dsu = DSU(n)
answers = []

for opr, u, v in reversed(oprs):
    if opr == "ask":
        answers.append("YES" if dsu.find(u) == dsu.find(v) else "NO")
    else: 
        dsu.union(u, v)

print("\n".join(reversed(answers)))
