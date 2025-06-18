# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        mod = 10**9 + 7
        res = 0

        for i, n in enumerate(arr):
            while stack and n<stack[-1][1]:
                j, m = stack.pop()
                l = j - stack[-1][0] if stack else j + 1
                r = i-j
                res = (res + m*l*r) % mod
            stack.append((i, n))
        for i in range(len(stack)):
            j, n = stack[i]
            l = j - stack[i-1][0] if i > 0 else j+1
            r = len(arr) - j
            res = (res + n*l*r) % mod
        return res