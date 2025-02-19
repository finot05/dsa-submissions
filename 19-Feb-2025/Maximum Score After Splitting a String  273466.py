# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        score = 0
        ones_psum = [int(num) for num in s]
        ones_psum.append(0)
        for i in range(n-1, -1, -1):
            ones_psum[i] += ones_psum[i+1]
        running = 0
        for i in range(n-1):
            if s[i] == '0':
                running += 1
            curr_score = running + ones_psum[i+1]
            score = max(score, curr_score)
        return score
            
            