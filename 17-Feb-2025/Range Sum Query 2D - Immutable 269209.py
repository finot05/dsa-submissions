# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if 0 < i:
                    self.matrix[i][j] += self.matrix[i-1][j]
                if 0 < j:
                    self.matrix[i][j] += self.matrix[i][j-1]
                if  0 < i and 0 < j:
                    self.matrix[i][j] -= self.matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2]
        if col1 != 0:
            ans -= self.matrix[row2][col1-1]
        if row1 != 0:
            ans -= self.matrix[row1-1][col2]
        if col1 != 0 and row1 != 0:
            ans += self.matrix[row1-1][col1-1]
        
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)