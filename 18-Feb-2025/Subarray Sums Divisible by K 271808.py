# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        current_sum = 0
        count = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum % k in prefix_sum_count:
                count += prefix_sum_count[current_sum % k]
            prefix_sum_count[current_sum % k] += 1
        
        return count     