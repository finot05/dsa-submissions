# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def solve_tree(p):
    n = len(p)
    
    def dfs(l, r):
        if l == r:
            return (p[l], p[l], 0)
        
        mid = (l + r) // 2
        l_min, l_max, l_ops = dfs(l, mid)
        r_min, r_max, r_ops = dfs(mid+1, r)
        
        if l_ops == -1 or r_ops == -1:
            return (-1, -1, -1)
        
        if l_max <= r_min:
            return (min(l_min, r_min), max(l_max, r_max), l_ops + r_ops)
        elif r_max <= l_min:
            return (min(l_min, r_min), max(l_max, r_max), l_ops + r_ops + 1)
        else:
            return (-1, -1, -1)
    
    _, _, ops = dfs(0, n-1)
    return ops

t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    print(solve_tree(p))