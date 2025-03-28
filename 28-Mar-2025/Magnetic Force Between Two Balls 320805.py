# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # l, h = 0, max(position)
        position.sort()
        def canPlaceBalls(f):
            count = 1
            last_p = position[0]
            for i in range(1, len(position)):
                if position[i] - last_p >= f:
                    count += 1
                    last_p = position[i]
                    if count == m:
                        return True
            return False
        l, h = 1, position[-1] - position[0]
        max_f = 1
        while l<=h:
            mid = (l+h)//2
            if canPlaceBalls(mid):
                max_f = mid
                l = mid+1
            else:
                h = mid-1
        return max_f