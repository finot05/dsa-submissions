# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    r_max = 0
    r_sum = 0
    for num in r:
        r_sum += num
        r_max = max(r_max, r_sum)

    b_max = 0
    b_sum = 0
    for num in b:
        b_sum += num
        b_max = max(b_max, b_sum)

    print(r_max + b_max)
