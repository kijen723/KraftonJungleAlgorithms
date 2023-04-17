# https://www.acmicpc.net/problem/17608

import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for i in range(N)]

see, count = 0, 0

for i in range(N):
    if see < heights[-1]:
        see = heights.pop()
        count += 1
    else:
        heights.pop()
print(count)
