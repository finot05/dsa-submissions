# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    l, r = 0, 1
    c = 0
    if n <= 1:
        print(0)
        continue
    while r<n:
        if p[l] > p[r]:
            c += 1
            l += 1
            r += 1
        l += 1
        r += 1

    print(c)
