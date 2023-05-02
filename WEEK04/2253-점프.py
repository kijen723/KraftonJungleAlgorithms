# https://www.acmicpc.net/problem/2253

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[sys.maxsize] * (int((2 * N) ** 0.5) + 2) for i in range(N + 1)]
dp[1][0] = 0

small = [int(input()) for i in range(M)]
    
for i in range(2, N + 1):
    if i in small:
        continue
    for j in range(1, int((2 * N) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        
if min(dp[N]) == sys.maxsize:
    print(-1)
else:
    print(min(dp[N]))