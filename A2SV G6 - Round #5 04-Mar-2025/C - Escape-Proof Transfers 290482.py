# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = map(int, input().split())
s = list(map(int, input().split()))
valid = 0
count = 0
for i in range(n):
    if s[i] <= t:
        valid += 1
    else:
        valid = 0
    if valid >= c:
        count += 1
print(count)
