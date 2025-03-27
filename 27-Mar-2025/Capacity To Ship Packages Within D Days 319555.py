# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            curr_weight = 0
            required_days = 1  
            
            for weight in weights:
                if curr_weight + weight > capacity:
                    required_days += 1
                    curr_weight = 0 
                curr_weight += weight
            
            return required_days <= days
        
        l, r = max(weights), sum(weights)  
        
        while l < r:
            mid = (l + r) // 2
            if valid(mid): 
                r = mid
            else:
                l = mid + 1 
        
        return l