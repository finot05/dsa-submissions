# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [(i, num) for num, i in enumerate(a)]
    a.sort()
    b.sort()
    # print(a)
    # print(b)
    ans = [0] * n
    for i in range(n):
        # print(a[i])
        ans[a[i][1]] = b[i]
    print(*ans)