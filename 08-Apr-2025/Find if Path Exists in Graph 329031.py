# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in freq[node]:
                if neighbour not in visited and dfs(neighbour, visited):
                    return True
            return False
        
        freq = defaultdict(list)
        for i, j in edges:
            freq[i].append(j)
            freq[j].append(i)
        return dfs(source, set())