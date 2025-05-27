# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, path):
            if i == len(s):
                ans.append(''.join(path))
                return
            if s[i].isalpha():
                backtrack(i+1, path + [s[i].lower()])
                backtrack(i+1, path + [s[i].upper()])
            else:
                backtrack(i+1, path + [s[i]])

        backtrack(0, [])
        return ans

