# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            start, end = max(a1, b1), min(a2, b2)
            if start <= end:
                ans.append([start, end])
            if a2 > b2:
                j += 1
            else:
                i += 1
        return ans