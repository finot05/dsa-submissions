# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l_b = bisect_left(nums, target)
        # print(l_b)
        if l_b >= len(nums) or nums[l_b] != target:
            return [-1, -1]
        h_b = bisect_right(nums, target)
        return [l_b, h_b-1]