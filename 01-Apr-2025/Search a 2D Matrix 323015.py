# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        l, h = 0, m - 1
        while l <= h:
            mid = (l + h) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]: 
                break
            elif matrix[mid][0] > target: 
                h = mid - 1
            else:
                l = mid + 1
        else:
            return False 

        row = matrix[mid]
        idx = bisect_left(row, target) 
        return idx < n and row[idx] == target