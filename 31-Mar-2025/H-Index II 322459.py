# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        ans = 0
        
        while l <= r:
            mid = (l + r) // 2
            h = n - mid 
            if citations[mid] >= h:
                ans = h 
                r = mid - 1 
            else:
                l = mid + 1  
        return ans