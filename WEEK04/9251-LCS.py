# https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

fst = input().rstrip()
snd = input().rstrip()

lenfst = len(fst)
lensnd = len(snd)

dp = [0] * max(lenfst, lensnd)

for i in range(lenfst):
    count = 0
    for j in range(lensnd):
        if count < dp[j]:
            count = dp[j]
        elif fst[i] == snd[j]:
            dp[j] = count + 1
            
print(max(dp))