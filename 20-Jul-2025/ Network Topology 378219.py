# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict, Counter
n, m = map(int, input().split())
graph = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += 1
    graph[y] += 1
degree_count = Counter(graph.values())
if len(degree_count) == 1 and 2 in degree_count and m == n:
    print("ring topology")
elif degree_count.get(1) == 2 and degree_count.get(2) == n - 2 and m == n - 1:
    print("bus topology")
elif degree_count.get(1) == n - 1 and degree_count.get(n - 1) == 1 and m == n - 1:
    print("star topology")
else:
    print("unknown topology")