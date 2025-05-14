# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        power_set = []
        for mask in range(1<<n):
            subset = []
            for i in range(n):
                if mask & (1<<i):
                    subset.append(nums[i])
            power_set.append(subset)
        
        return power_set