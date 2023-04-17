# https://www.acmicpc.net/problem/1655

import heapq
import sys
input = sys.stdin.readline

N = int(input())
minheap = []
maxheap = []

for i in range(N):
    num = int(input())

    if len(minheap) == len(maxheap):
        heapq.heappush(minheap, -num)
    else:
        heapq.heappush(maxheap, num)

    if maxheap and -minheap[0] > maxheap[0]:
        temp = -heapq.heappop(minheap)
        heapq.heappush(minheap, -heapq.heappop(maxheap))
        heapq.heappush(maxheap, temp)

    print(-minheap[0])
