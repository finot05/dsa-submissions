# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, min(ranks) * cars * cars  

        def canRepairInTime(T):
            total_cars = 0
            for r in ranks:
                total_cars += isqrt(T // r) 
                if total_cars >= cars:
                    return True 
            return False

        while low < high:
            mid = (low + high) // 2
            if canRepairInTime(mid):
                high = mid
            else:
                low = mid + 1

        return low