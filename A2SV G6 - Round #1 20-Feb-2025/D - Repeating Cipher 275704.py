# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
s = input()
ans = []
k, i = 1, 0
while i < len(s):
    ans.append(s[i])
    i += k
    k += 1
print(''.join(ans))