# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        current_sum = 0
        count = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum-goal in prefix_sum_count:
                count += prefix_sum_count[current_sum-goal]
            prefix_sum_count[current_sum] += 1
        
        return count   