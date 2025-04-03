# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        nums.sort()
        while l<=h:
            mid = (l+h)//2
            if nums[mid] > mid:
                h = mid-1
            else:
                l = mid+1
        return l