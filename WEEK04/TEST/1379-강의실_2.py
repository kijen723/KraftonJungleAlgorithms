# https://www.acmicpc.net/problem/1379

import sys, heapq
input = sys.stdin.readline

N = int(input())
lectures = sorted([list(map(int, input().split())) for i in range(N)], key = lambda x : (x[1], x[2]))
lecture = [0 for i in range(N + 1)]
room = [i for i in range(1, N + 1)]
    
heap = []
for num, start, end in lectures:
    while heap and heap[0][0] <= start:
        e, n = heapq.heappop(heap)
        heapq.heappush(room, n)
        
    n = heapq.heappop(room)
    heapq.heappush(heap, [end, n])
    lecture[num] = n
    
print(max(lecture))
for i in lecture[1:]:
    print(i)