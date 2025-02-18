# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()

    for i in range(n):
            if h[2*n-i-1] -h[n -1-i] < x:
                print("NO")
                break
    else:
        print("YES")