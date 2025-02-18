# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0]*len(nums)
        for start, end in requests:
            freq[start] += 1
            if end + 1 < len(freq):
                freq[end + 1] -= 1
        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq.sort(reverse = True)
        nums.sort(reverse = True)
                
        for i in range(len(nums)):
            nums[i] *= freq[i]
        return sum(nums)  % (10**9 + 7)   