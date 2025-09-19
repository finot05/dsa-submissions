# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
sys.setrecursionlimit(2 * 10**6)
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = list(range(n+2))
    
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

n, m = map(int, input().split())
dsu = DSU(n)

out = []
for _ in range(m):
    s, x = input().split()
    x = int(x)
    if s == '-':
        dsu.p[x] = dsu.find(x+1) 
    else:
        ans = dsu.find(x)
        if ans == n+1:
            out.append("-1")
        else:
            out.append(str(ans))

sys.stdout.write("\n".join(out))
