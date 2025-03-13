# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def construct(n):
            if n == 1:
                return '0'
            prev_str = construct(n-1)
            inverted_str = ''.join('1' if num == '0' else '0' for num in reversed(prev_str) )
            return prev_str + '1' + inverted_str
        new_n = construct(n)
        return new_n[k-1]