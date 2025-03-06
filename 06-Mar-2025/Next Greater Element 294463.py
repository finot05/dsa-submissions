# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1]
