# https://www.acmicpc.net/problem/1904

import sys
input = sys.stdin.readline

N = int(input())

dp = []
count = 0
for i in range(0, N):
    if i == 0:
        count = 1
    elif i == 1:
        count = 2
    else:
        count = (dp[-1] + dp[-2]) % 15746
    dp.append(count)
    
print(dp[N - 1])