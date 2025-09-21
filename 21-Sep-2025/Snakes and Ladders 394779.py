# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        moves = [-1] * (n*n + 1)
        idx = 1
        for r in range(n-1, -1, -1):
            row = board[r] if (n-1-r) % 2 == 0 else board[r][::-1]
            for val in row:
                moves[idx] = val
                idx += 1
        
        queue = deque()
        queue.append((1, 0))
        visited = set()
        visited.add(1)
        
        while queue:
            pos, steps = queue.popleft()
            if pos == n*n:
                return steps
            for i in range(1, 7):
                nxt = pos + i
                if nxt > n*n:
                    continue
                if moves[nxt] != -1:
                    nxt = moves[nxt]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1