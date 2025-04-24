# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [0]*n

        def dfs(node):
            if safe[node] == 1:
                return False
            if safe[node] == 2:
                return True
            safe[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node] = 2
            return True
            
        safe_nodes = [i for i in range(n) if dfs(i)]
        return sorted(safe_nodes)