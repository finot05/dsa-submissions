# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        rls = 0
        for char in s:
            if char == 'R':
                rls += 1
            else:
                rls -= 1
            if not rls:
                count += 1
        return count