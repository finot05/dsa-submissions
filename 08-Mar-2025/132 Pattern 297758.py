# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        curMin = nums[0]
        for num in nums[1:]:
            while stk and stk[-1][0] <= num:
                stk.pop()
            if stk and stk[-1][1] < num:
                return True
            stk.append([num, curMin])
            curMin = min(curMin, num)
        return False
