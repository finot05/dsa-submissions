# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0]*n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        while n > 2:
            size = len(leaves)
            n -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)
        
        return list(leaves)
                
