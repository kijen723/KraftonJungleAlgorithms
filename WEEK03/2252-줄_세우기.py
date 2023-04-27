# https://www.acmicpc.net/problem/2252

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tall = [[] for i in range(N + 1)]
topology = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    tall[a].append(b)
    topology[b] += 1

queue = deque()
for i in range(1, N + 1):
    if topology[i] == 0:
        queue.append(i)

answer = []
while queue:
    student = queue.popleft()
    answer.append(student)
    for i in tall[student]:
        topology[i] -= 1
        if topology[i] == 0:
            queue.append(i)

print(*answer)
