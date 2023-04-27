# https://www.acmicpc.net/problem/1432

import heapq
import sys
input = sys.stdin.readline

def topology_sort():
    queue = []
    for i in range(1, N + 1):
        if topology[i] == 0:
            heapq.heappush(queue, -i)
            
    NN = N
    while queue:
        node = -heapq.heappop(queue)
        answer[node] = NN
        
        for i in nodes[node]:
            topology[i] -= 1
            if topology[i] == 0:
                heapq.heappush(queue, -i)
        
        NN -= 1

N = int(input())
nodes = [[] for i in range(N + 1)]
topology = [0] * (N + 1)

for i in range(1, N + 1):
    temp = [0] + list(map(int, input().strip()))
    for j in range(1, N + 1):
        if temp[j] == 1:
            nodes[j].append(i)
            topology[i] += 1
            
answer = [0] * (N + 1) 

topology_sort()
if answer.count(0) > 1:
    print(-1)
else:
    print(*answer[1:])