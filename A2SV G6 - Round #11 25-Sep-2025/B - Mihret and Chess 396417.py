# Problem: B - Mihret and Chess - https://codeforces.com/gym/604781/problem/B

l1, r1, l2, r2 = map(int, input().split())

ans = [0]*3

ans[0] = 1 if(l1 == l2 or r1 == r2) else 2

if (r1 + l1) % 2 != (r2 + l2) % 2:
    ans[1] = 0
elif abs(r1 - r2) == abs(l1 - l2):
    ans[1] = 1
else:
    ans[1] = 2

ans[2] = max(abs(r1 - r2), abs(l1 - l2))
print(*ans)