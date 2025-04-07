# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canBeDividedToK(max_sum):
            div = 1
            temp = 0
            for num in nums:
                if temp+num > max_sum:
                    temp = num
                    div += 1
                else:
                    temp += num
            return div <= k
        
        l, h = max(nums), sum(nums)
        while l<=h:
            mid = (h+l)//2
            if canBeDividedToK(mid):
                h = mid-1
            else:
                l = mid+1
        return l