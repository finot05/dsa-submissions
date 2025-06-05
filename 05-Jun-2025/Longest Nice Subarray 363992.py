# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        cur = 0
        res = 0

        for r in range(len(nums)):
            while cur & nums[r]:
                cur ^= nums[l]
                l += 1
            cur |= nums[r]
            res = max(res, r - l + 1)

        return res
