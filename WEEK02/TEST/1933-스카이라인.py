# https://www.acmicpc.net/problem/1933

import heapq
import sys
input = sys.stdin.readline

N = int(input())
buildings = []
for i in range(N):
    L, H, R = map(int, input().split())
    buildings.append((L, 0, H, R))
    buildings.append((R, 1, H, None))

buildings.sort(key=lambda x: (x[0], x[1], -x[2]))

tempheight = 0
answer = []
proceeding = []
check = set()

for i in range(N * 2):
    location, updown, height, end = buildings[i]

    if updown == 0:
        if tempheight < height:
            tempheight = height
            answer.append((location, height))
        heapq.heappush(proceeding, (-height, end))
    else:
        check.add(location)

        while proceeding:
            if proceeding[0][1] not in check:
                break
            heapq.heappop(proceeding)

        if not proceeding:
            if tempheight:
                tempheight = 0
                answer.append((location, tempheight))
        else:
            if -proceeding[0][0] < tempheight:
                tempheight = -proceeding[0][0]
                answer.append((location, tempheight))

for i in answer:
    print(*i, end='')
    print(' ', end='')
