# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        actual = 0
        for i, num in enumerate(nums):
            expected ^= i+1
            actual ^= num
        return expected ^ actual
