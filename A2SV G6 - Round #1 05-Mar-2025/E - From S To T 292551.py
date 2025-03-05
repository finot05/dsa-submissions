# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import defaultdict

def can_transform(s, t, p):
    s_index = 0
    for char in t:
        if s_index < len(s) and s[s_index] == char:
            s_index += 1
    if s_index != len(s):
        return "NO"

    s_count = defaultdict(int)
    t_count = defaultdict(int)
    p_count = defaultdict(int)

    for char in s:
        s_count[char] += 1
    for char in t:
        t_count[char] += 1
    for char in p:
        p_count[char] += 1

    for char in t_count:
        if s_count[char] + p_count[char] < t_count[char]:
            return "NO"

    return "YES"

q = int(input())
results = []
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    results.append(can_transform(s, t, p))

print("\n".join(results))
