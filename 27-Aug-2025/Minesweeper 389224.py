# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        q = deque([(r, c)])
        while q:
            r, c = q.popleft()

            mines = 0
            neighbors = []
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == "M":
                        mines += 1
                    else:
                        neighbors.append((nr, nc))

            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = "B"
                for nr, nc in neighbors:
                    if board[nr][nc] == "E":
                        q.append((nr, nc))
                        board[nr][nc] = "B"  

        return board