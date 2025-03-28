# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canAllChildGet(c):
            div = sum(num//c for num in candies)
            return div >= k
        
        l, h = 1, max(candies)
        max_c = 0
        while l<=h:
            mid = (l+h)//2
            if canAllChildGet(mid):
                max_c = mid
                l = mid+1
            else:
                h = mid-1
        return max_c