# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        invalid = -1
        min_idx = -1
        max_idx = -1
        c = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                invalid = i
            if nums[i] == minK:
                min_idx = i
            if nums[i] == maxK:
                min_idx = i
            c += max(min(min_idx, max_idx)- invalid, 0)
        return c
