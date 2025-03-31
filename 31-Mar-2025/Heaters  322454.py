# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def canCover(r):
            for h in houses:
                index = bisect.bisect_left(heaters, h)

                left_heater = float('inf') if index == 0 else h - heaters[index - 1]
                right_heater = float('inf') if index == len(heaters) else heaters[index] - h
                
                if min(left_heater, right_heater) > r:
                    return False
            return True

        l, h = 0, max(max(houses), max(heaters))- min(houses)
        while l < h:
            mid = (l + h) // 2
            if canCover(mid):
                h = mid 
            else:
                l = mid + 1 
        return l