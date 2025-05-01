# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while len(nums) >= 2 and nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            val = (min(x, y) * 2 + max(x, y))
            heappush(nums, val)
            count += 1  
        return count
        