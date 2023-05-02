# https://www.acmicpc.net/problem/11049

import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for i in range(N)]

dp = [[0] * N for i in range(N)]
for count in range(N - 1):
    for i in range(N - 1 - count):
        j = i + count + 1
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
            
print(dp[0][-1])