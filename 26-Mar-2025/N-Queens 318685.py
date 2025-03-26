# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = set()
        posdiag = set()
        negdiag = set()
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                ans.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (c - r) in posdiag or (c + r) in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(c - r)
                negdiag.add(c + r)
                board[c][r] = 'Q'
                
                backtrack(r + 1)
                
                col.remove(c)
                posdiag.remove(c - r)
                negdiag.remove(c + r)
                board[c][r] = '.'

        backtrack(0)
        return ans