# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pf = arr[:]
        for i in range(1, len(arr)):
            pf[i] ^= pf[i-1]
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(pf[r])
            else:
                ans.append(pf[r] ^ pf[l-1])
        return ans