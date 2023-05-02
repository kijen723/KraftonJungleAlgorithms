# https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline

n = int(input())

dp = []
num = 0
for i in range(n + 1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = dp[-1] + dp[-2]
    dp.append(num)
    
print(dp[-1])