# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0]* (len(s)+1)
        res = []
        for left, right, direction in shifts:
            if direction == 0:
                prefix_sum[left] += -1
                prefix_sum[right+1] += 1
            else:
                prefix_sum[left] += 1
                prefix_sum[right+1] += -1
        running = 0
        for i in range(len(s)):
            running += prefix_sum[i]
            temp = (ord(s[i]) + running - ord("a"))%26 + ord("a")
            res.append(chr(temp))
        return "".join(res)
