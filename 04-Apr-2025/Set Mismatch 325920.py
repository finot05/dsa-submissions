# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ex_sum = n*(n+1)//2
        uni_sum = sum(set(nums))
        missing = ex_sum - uni_sum
        dup = sum(nums) - uni_sum
    
        return [dup, missing]