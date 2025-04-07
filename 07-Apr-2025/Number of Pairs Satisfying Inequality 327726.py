# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        self.ans = 0
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums)//2
            l = merge_sort(nums[:mid])
            r = merge_sort(nums[mid:])
            
            j = 0
            for i in range(len(l)):
                while j < len(r) and l[i] > r[j]+diff:
                    j += 1
                self.ans += len(r) - j

            i = j = 0
            merged = []
            
            while i < len(l) and j < len(r):
                if r[j] < l[i]:
                    merged.append(r[j])
                    j += 1
                else:
                    merged.append(l[i])
                    i += 1
            merged += l[i:]
            merged += r[j:]
            return merged
        
        merge_sort(arr)
        return self.ans
