# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D

from collections import defaultdict
import heapq
n, m = map(int, input().split())
gp = defaultdict(list)
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    gp[a].append(b)
    indegree[b] += 1
heap = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)
res = []
while heap:
    u = heapq.heappop(heap)
    res.append(u)
    for v in gp[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(heap, v)
if len(res) == n:
    print(*res)
else:
    print(-1)
