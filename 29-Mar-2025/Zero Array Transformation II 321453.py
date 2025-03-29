# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        def canBeTransformed(m):
            diff = [0]*(len(nums)+1)
            for x, y, c in queries[:m]:
                diff[x]-=c
                diff[y+1]+=c
            for i in range(len(diff)-1):
                if i!=0:

                    diff[i]+=diff[i-1]
                if max(0, nums[i]+diff[i])>0:
                    return False
            
            return True
        
        l, h = 0, len(queries)
        ans = -1
        while l<=h:
            mid = (l+h)//2
            if canBeTransformed(mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans
                