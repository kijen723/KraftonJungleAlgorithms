# https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M + 1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(M + 1):
            if j >= coin:
                dp[j] += dp[j - coin]
                
    print(dp[M])