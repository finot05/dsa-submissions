# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            c = 0
            while i:
                c += i & 1
                i >>= 1
            ans.append(c)
        return ans