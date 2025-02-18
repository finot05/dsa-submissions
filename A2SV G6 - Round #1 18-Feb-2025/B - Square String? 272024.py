# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n % 2 != 0:
        print('NO')
    else:
        for i in range(n//2):
            if s[i] != s[n//2+i]:
                print('NO')
                break
        else:
            print('YES')