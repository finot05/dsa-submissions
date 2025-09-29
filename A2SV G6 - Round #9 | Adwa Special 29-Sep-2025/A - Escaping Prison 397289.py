# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    r = 0
    for _ in range(n):
        x, y = map(int, input().split())
        r += max(x, y)
    print("YES" if r >= h else "NO")