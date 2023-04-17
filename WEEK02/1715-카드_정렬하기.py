# https://www.acmicpc.net/problem/1715

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
answer = 0

for i in range(N):
    heapq.heappush(heap, int(input()))

while len(heap) > 1:
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    answer += temp
    heapq.heappush(heap, temp)

print(answer)
