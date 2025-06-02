# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans  = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (1<<i) & num:
                    count += 1

            res1 = count*count*len(nums)
            res2 = count*(len(nums) - count)*count
            if (res1 + res2) & 1:
                ans |= (1<<i)
        return ans

