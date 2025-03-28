# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""

        _set = set(s)
        for i in range(len(s)):
            ch = s[i]
            if ch.swapcase() not in _set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) < len(right):
                    return right
                return left
        return s
