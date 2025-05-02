# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = [] 
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heapq.heappush(min_heap, diff)

                if len(min_heap) > ladders:
                    smallest = heapq.heappop(min_heap)
                    bricks -= smallest

                if bricks < 0:
                    return i
        
        return len(heights) - 1