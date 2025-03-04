# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        c = 1
        points.sort(key = lambda x:(x[1], x[0]))
        print(points)
        r = 1
        s, e = points[0]
        while r < n:
            if e < points[r][0]:
                c += 1
                s, e = points[r]
            r += 1
            # if r < n and points[r][0] > points[r-1][0]:
            #     s = points[r][0]
            # if r < n and points[r][1] < points[r-1][1]:
            #     e = points[r][1]
            
        return c