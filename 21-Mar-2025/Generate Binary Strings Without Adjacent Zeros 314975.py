# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        def backtrack(idx, path):
            if idx >= n:
                if path and path[-1] == '0' and idx != 0 or path[-1] == '1':
                    self.ans.append("".join(path))
                return
            for i in range(2):
                if path and path[-1] == '0' and i == 0:
                    continue
                path.append(str(i%2))
                backtrack(idx+1, path)
                path.pop()
        backtrack(0, [])
        return self.ans