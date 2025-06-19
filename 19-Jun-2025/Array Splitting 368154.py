# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == n:
    print(0)
    exit()
gaps = []
for i in range(n-1):
    gaps.append(a[i+1] - a[i])
gaps.sort()
print(sum(gaps[:n-k]))
