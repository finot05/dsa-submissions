# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
v = list(map(int, input().split()))
pf1 = [0] + v
pf2 = [0] + sorted(v)
for i in range(1, n+1):
    pf1[i] += pf1[i-1]
    pf2[i] += pf2[i-1]
# print(pf2, pf1)
m = int(input())
for i in range(m):
    type, l, r = map(int, input().split())
    print(pf1[r] - pf1[l-1] if type == 1 else pf2[r] - pf2[l-1])
