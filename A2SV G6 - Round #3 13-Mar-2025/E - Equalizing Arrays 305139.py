# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

if sum(a) != sum(b):
    print(-1)
    exit()
f, s = 0, 0
c = 0
# cur1, cur2 = 0, 0
while f < n and s < m:
    if a[f] == b[s]:
        c += 1
        f += 1
        s += 1
    elif a[f] < b[s]:
        f += 1
        if f < n:
            a[f] += a[f-1]
    else:
        s += 1
        if s < m:
            b[s] += b[s-1]
print(c if c != 0 else -1) 