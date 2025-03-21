# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, rem):
            if not rem:
                ans.append(path[:])
                return
            
            for i in range(len(rem)):
                new_p = path + [rem[i]]
                new_rem = rem[:i] + rem[i+1:]
                backtrack(new_p, new_rem)
        backtrack([], nums)
        return ans