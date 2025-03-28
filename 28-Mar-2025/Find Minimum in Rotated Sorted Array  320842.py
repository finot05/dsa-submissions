# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1 
        while l < h: 
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
                
        return nums[l]