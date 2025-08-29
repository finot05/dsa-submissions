# Problem: Trapped in the Witch's Labyrinth - https://codeforces.com/problemset/problem/2034/C

import sys
import threading

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        matrix = [list(input().strip()) for _ in range(n)]

        status = [["U"] * m for _ in range(n)]
        
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < m):
                return "E"  
            if status[r][c] == "T" or status[r][c] == "E":
                return status[r][c] 
            if status[r][c] == "V":
                return "T" 
            status[r][c] = "V" 

            if matrix[r][c] == "?":
                nxt = [(r + dr, c + dc) for dr, dc in directions.values() if 0 <= r + dr < n and 0 <= c + dc < m]
                cell_status = "E"
                for nr, nc in nxt:
                    if dfs(nr, nc) == "T":
                        cell_status = "T"
                        break
                status[r][c] = cell_status
                return cell_status
            else:
                dr, dc = directions[matrix[r][c]]
                res = dfs(r + dr, c + dc)
                status[r][c] = res
                return res

        for i in range(n):
            for j in range(m):
                if status[i][j] == "U":
                    dfs(i, j)

        trapped_count = sum(status[i][j] == "T" for i in range(n) for j in range(m))
        print(trapped_count)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
