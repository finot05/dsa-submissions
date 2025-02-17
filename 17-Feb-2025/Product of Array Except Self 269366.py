# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * (n+1)
        suffix_prod = 1
        for i in range(n):
            prefix_prod[i+1] = prefix_prod[i] * nums[i]
            
        for i in range(n):
            prefix_prod[n-i-1] *= suffix_prod
            suffix_prod *= nums[n-1-i]
        return prefix_prod[:n]