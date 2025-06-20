# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

n = int(input())
p = [int(input()) for _ in range(n - 1)]

from collections import defaultdict

tree = defaultdict(list)
for child, parent in enumerate(p, start=2):
    tree[parent].append(child)
# print(tree)
for node in tree:
    children = 0
    for child in tree[node]:
        if child not in tree:
            children += 1
    if children < 3:
        print("No")
        exit()
print("Yes")

