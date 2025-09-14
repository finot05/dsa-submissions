# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()

        if all(ch == '-' for ch in s):
            print(n)
            continue

        if '<' not in s or '>' not in s:
            print(n)
            continue

        ans = 0
        for i in range(n):
            if s[i] == '-' or s[(i - 1) % n] == '-':
                ans += 1
        print(ans)
solve()