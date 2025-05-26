# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num3 = 0
        if len(nums2) & 1:
            for num1 in nums1:
                num3 ^= num1
        if len(nums1) & 1:
            for num2 in nums2:
                num3 ^= num2
        return num3