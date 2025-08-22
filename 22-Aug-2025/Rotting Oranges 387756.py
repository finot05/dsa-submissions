# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        minutes = 0
        
        while q:
            r, c, t = q.popleft()
            minutes = max(minutes, t)
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr <m and 0 <= nc <n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t+1))

        return -1 if fresh > 0 else minutes