# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dp(l, r):
            if l == r:
                return nums[l] 

            pick_left = nums[l] - dp(l + 1, r)
            pick_right = nums[r] - dp(l, r - 1)

            return max(pick_left, pick_right)

        return dp(0, len(nums) - 1) >= 0