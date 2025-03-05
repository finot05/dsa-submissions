# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
def min_tv_sub(n, k, d, a):
    sub_arr = Counter(a[:d])
    res = len(sub_arr)
    for i in range(d, n):
        sub_arr[a[i]] += 1
        if sub_arr[a[i - d]] > 0:
            sub_arr[a[i - d]] -= 1
        if sub_arr[a[i - d]] == 0:
            del sub_arr[a[i - d]]
        res = min(res, len(sub_arr))
    return res



t = int(input())
results = []
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    results.append(str(min_tv_sub(n, k, d, a)))

print('\n'.join(results))