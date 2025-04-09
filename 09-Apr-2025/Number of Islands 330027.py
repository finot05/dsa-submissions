# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            visited.add((row,col))
            if grid[row][col] == "0":
                return
            for dr, dc in directions:
                new_r, new_c = row+dr, col+dc 
                if inbound(new_r, new_c) and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
        
        directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
        visited = set()
        inbound = lambda row, col: 0<= row< len(grid) and 0<=col<len(grid[-1])
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == "1":
                    ans += 1
                    visited.add((r, c))
                    dfs(r, c)

        return ans