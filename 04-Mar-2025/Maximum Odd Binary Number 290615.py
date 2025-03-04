# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ls = ['0'] * n
        ls[-1] = '1'
        ones = sum(1 for num in s if num == '1')
        for i in range(ones-1):
            ls[i] = '1'
        return ''.join(ls)