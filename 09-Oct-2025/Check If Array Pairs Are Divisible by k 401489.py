# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0 for i in range(k)]
        for num in arr:
            freq[num%k] += 1
        for i in range(1,k):
            if i != k-i:
                if freq[i] != freq[k-i]:
                    return False
            else:
                if freq[i] & 1:
                    return False
        return True