# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    ans = []
    if max(b, c)>=a:
        ans.append(max(b, c) - a + 1)
    else:
        ans.append(0)
    if max(a, c) >= b:
        ans.append(max(a, c) - b + 1)  
    else:
        ans.append(0)
    if max(a, b) >= c:
        ans.append(max(a, b) - c + 1)
    else:
        ans.append(0)
    print(*ans)