# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from itertools import accumulate
n, k, q = map(int, input().split())
recipes = []
for i in range(n):
    recipe = list(map(int, input().split()))
    recipes.append(recipe)
# max_value = max(max(recipe) for recipe in recipes)
max_value = 200000
freq = [0] * (max_value+2)

for start, end in recipes:
    freq[start] += 1
    freq[end + 1] -= 1

for i in range(1, len(freq)):
    freq[i] += freq[i - 1]

freq_sum = [0]*len(freq)
for i in range(len(freq)):
    if freq[i] >= k:
        freq_sum[i] = 1
    
# for i in range(1, len(freq_sum)):
#     freq_sum[i] += freq_sum[i - 1] 
freq_sum = list(accumulate(freq_sum))
# print(freq_sum)

for _ in range(q):
    start, end = map(int, input().split())
    print(freq_sum[end] - freq_sum[start-1])