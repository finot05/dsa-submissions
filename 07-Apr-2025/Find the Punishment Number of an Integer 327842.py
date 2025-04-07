# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def permutation(i, cur, target, string):
            if i == len(string) and cur == target:
                return True
            for j in range(i, len(string)):
                string[i:j+1]
                if permutation(j+1, cur + int(string[i:j+1]) , target, string):
                    return True
            return False

        ans = 0
        for i in range(1, n+1):
            if permutation(0, 0, i, str(i*i)):
                ans += i*i
            
        return ans