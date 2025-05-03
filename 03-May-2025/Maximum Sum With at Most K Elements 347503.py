# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        for r in range(n):
            grid[r] = [-num for num in grid[r]]
            heapify(grid[r])

        max_hp = []
        for r in range(n):
            if grid[r] and limits[r] > 0:
                heappush(max_hp, (grid[r][0], r))

        tot = 0
        used = [0] * n
        while k>0 and max_hp:
            val, r = heappop(max_hp)
            tot += -val
            used[r] += 1
            heappop(grid[r])
            k -= 1
            if grid[r] and used[r] < limits[r]:
                heappush(max_hp, (grid[r][0], r))

        return tot
