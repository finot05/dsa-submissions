# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(num):
            if len(path) == k:
                ans.append(path[:])
                return
            # if num > n:
            #     return
            # path.append(num)
            # backtrack(num+1)

            # path.pop()
            # backtrack(num+1)
        
            for i in range(num, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()

        backtrack(1)
        return ans