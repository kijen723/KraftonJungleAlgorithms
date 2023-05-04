# https://www.acmicpc.net/problem/1890

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
dp = [[0] * N for i in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[N-1][N-1])
            break
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]