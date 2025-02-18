# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        current_sum = 0
        count = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum-k in prefix_sum_count:
                count += prefix_sum_count[current_sum-k]
            prefix_sum_count[current_sum] += 1

        
        return count        