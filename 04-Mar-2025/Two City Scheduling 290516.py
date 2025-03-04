# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        temp = [(a - b, a, b) for a, b in costs]        
        temp.sort()
        total_cost = 0
        for i in range(len(temp)):
            if i < n: 
                total_cost += temp[i][1]  
            else: 
                total_cost += temp[i][2]
        
        return total_cost