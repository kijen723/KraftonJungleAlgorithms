# https://www.acmicpc.net/problem/2637

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parts = [[] for i in range(N + 1)]
need = [[0] * (N + 1) for i in range(N + 1)]
topology = [0] * (N + 1)
basic = []
for i in range(M):
    X, Y, K = map(int, input().split())
    parts[Y].append((X, K))
    topology[X] += 1

queue = deque()
for i in range(1, N + 1):
    if topology[i] == 0:
        queue.append(i)
        basic.append(i)

while queue:
    number = queue.popleft()
    for part, count in parts[number]:
        if number in basic:
            need[part][number] = count
        else:
            for i in range(1, N + 1):
                need[part][i] += need[number][i] * count
        topology[part] -= 1
        if topology[part] == 0:
            queue.append(part)

for i in basic:
    print(i, need[N][i])
