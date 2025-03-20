# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(idx, subset):
            if idx >= len(nums):
                self.ans.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx+1, subset)

            subset.pop()
            backtrack(idx+1, subset)
        backtrack(0, [])
        return self.ans