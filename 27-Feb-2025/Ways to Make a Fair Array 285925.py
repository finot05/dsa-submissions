# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_prefix, odd_prefix = 0, 0  
        total_even, total_odd = 0, 0 
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even += num
            else:
                total_odd += num
        
        count = 0  

        for i, num in enumerate(nums):
            if i % 2 == 0:  
                total_even -= num
            else:  
                total_odd -= num
            
            if even_prefix + total_odd == odd_prefix + total_even:
                count += 1
            
            if i % 2 == 0:
                even_prefix += num
            else:
                odd_prefix += num

        return count
 