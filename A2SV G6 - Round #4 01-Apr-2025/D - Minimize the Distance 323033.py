# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
s = list(map(int, input().split()))
s.sort()
print(s[(n - 1) // 2])