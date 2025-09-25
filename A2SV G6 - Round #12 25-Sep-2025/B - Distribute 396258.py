# Problem: B - Distribute - https://codeforces.com/gym/606404/problem/B

n = int(input())
a = list(map(int, input().split()))
indx = list(enumerate(a))
indx.sort(key=lambda x: x[1])
# print(indx)
for i in range(n//2):
    print(indx[i][0]+1, indx[n-i-1][0]+1)