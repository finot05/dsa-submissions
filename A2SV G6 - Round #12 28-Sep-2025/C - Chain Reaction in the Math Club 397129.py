# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

ans = 0

while True:
    q = deque([i for i in range(1, n + 1) if degree[i] == 1])
    if not q:
        break 
    ans += 1
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if degree[nei] > 0:  
                degree[nei] -= 1
        degree[node] = 0  

print(ans)
