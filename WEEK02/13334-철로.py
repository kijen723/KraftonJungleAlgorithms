# https://www.acmicpc.net/problem/13334

import heapq
import sys
input = sys.stdin.readline

n = int(input())
startend = [sorted(list(map(int, input().split()))) for i in range(n)]
d = int(input())

abileroute = []
for i in startend:
    if i[1] - i[0] <= d:
        abileroute.append(i)
abileroute.sort(key=lambda x: x[1])

heap = []
answer = 0

for i in abileroute:
    if not heap:
        heapq.heappush(heap, i)
    else:
        while heap[0][0] < i[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, i)
    answer = max(answer, len(heap))

print(answer)
