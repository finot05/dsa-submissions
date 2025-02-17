# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input()) 

for _ in range(t):
    n, m = map(int, input().split())  
    board = [list(map(int, input().split())) for _ in range(n)]  

    diag1 = {}  
    diag2 = {}   

    for r in range(n):
        for c in range(m):
            key1 = r - c
            key2 = r + c

            if key1 not in diag1:
                diag1[key1] = 0
            if key2 not in diag2:
                diag2[key2] = 0

            diag1[key1] += board[r][c]
            diag2[key2] += board[r][c]

    max_x_sum = 0
    for r in range(n):
        for c in range(m):
            x_sum = diag1[r - c] + diag2[r + c] - board[r][c] 
            max_x_sum = max(max_x_sum, x_sum)

    print(max_x_sum)