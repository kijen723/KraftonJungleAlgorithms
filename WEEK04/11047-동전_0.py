# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]

count = 0
for i in reversed(range(N)):
    count += K // coins[i]
    K %= coins[i]
    if K <= 0:
        break
    
print(count)