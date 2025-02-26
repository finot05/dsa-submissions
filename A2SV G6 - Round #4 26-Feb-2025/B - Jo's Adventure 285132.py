# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
pf = [0]
for i in range(n-1):
    pf.append(a[i]-a[i+1])
pff = pf
pfb = pf[1:] + [0]
# print(pf)
for i in range(1, len(pff)):
    if pff[i] > 0:
        pff[i] += pff[i-1]
    else:
        pff[i] = pff[i-1]
# print(pfb)
for i in range(len(pff)-2, -1, -1):
    if pfb[i] < 0:
        pfb[i] = abs(pfb[i]) + pfb[i+1]
    else:
        pfb[i] = pfb[i+1]
# print(pfb)
# print(pff)
# print(pfb)

for i in range(m):
    s, t = map(int, input().split())
    if s > t:
        print(pfb[t-1] - pfb[s-1] )
    else:
        print(pff[t-1] - pff[s-1])
