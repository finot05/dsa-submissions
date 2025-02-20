# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n = int(input())
ans = ""
for i in range(1,1001):
    ans += str(i)
print(ans[n-1])