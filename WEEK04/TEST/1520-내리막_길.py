# https://www.acmicpc.net/problem/1520

import sys
input = sys.stdin.readline

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    count = 0
    for i in range(4):
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        
        if 0 <= nx < M and 0 <= ny < N and heights[x][y] > heights[nx][ny]:
            count += dfs(nx, ny)
            
    dp[x][y] = count
    return dp[x][y]

M, N = map(int, input().split())
heights = [list(map(int, input().split())) for i in range(M)]
dp = [[-1] * N for i in range(M)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

print(dfs(0, 0))