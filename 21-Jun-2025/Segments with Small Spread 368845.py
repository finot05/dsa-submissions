# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

max_dq = deque()
min_dq = deque()
res = 0
l = 0

for r in range(n):
    while max_dq and a[r] > max_dq[-1]:
        max_dq.pop()
    max_dq.append(a[r])
    
    while min_dq and a[r] < min_dq[-1]:
        min_dq.pop()
    min_dq.append(a[r])
    
    while max_dq[0] - min_dq[0] > k:
        if max_dq[0] == a[l]:
            max_dq.popleft()
        if min_dq[0] == a[l]:
            min_dq.popleft()
        l += 1
    
    res += r - l + 1

print(res)
