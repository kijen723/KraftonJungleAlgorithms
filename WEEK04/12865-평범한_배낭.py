# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weights = [list(map(int, input().split())) for i in range(N)]
dp = [0] * (K + 1)

for W, V in weights:
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)
        
print(dp[-1])