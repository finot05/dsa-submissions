# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            g = 0
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                if g == k:
                    c += 1
                if g < k:
                    break
                
        return c