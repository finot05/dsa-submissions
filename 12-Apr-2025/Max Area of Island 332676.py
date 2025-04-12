# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        # inbound = lambda row, col: 0 <= row <len(grid) and 0 <= col < len(grid[0])
        def inbound(row, col): return 0 <= row <len(grid) and 0 <= col < len(grid[0])
        self.max_area = 0
        visited = set()
        def dfs(row, col):
            # cur_area = 1
            visited.add((row, col))
            # self.max_area = max(self.max_area, cur_area)
            cur_node_count = 1
            for r, c in directions:
                new_r = row + r
                new_c = col + c
                if inbound(new_r, new_c) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                    # cur_area += 1
                    count = dfs(new_r, new_c)
                    cur_node_count += count 

            return cur_node_count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cur_node_count = dfs(i, j)
                    self.max_area = max(self.max_area, cur_node_count)
                    # self.max_area = max(cur, self.max_area)
        return self.max_area