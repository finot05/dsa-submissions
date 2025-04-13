# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj_map = defaultdict(list)
        for team, nei in edges:
            adj_map[team].append(nei)

        def dfs(team, visited):
            for nei in adj_map[team]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, visited)
        
        for num in range(n):
            visited = set()
            dfs(num, visited)
            if len(visited) == n-1:
                return num
        return -1