# https://www.acmicpc.net/problem/18405

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        virus, x, y, time = queue.popleft()
        if time == S:
            return

        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]

            if 0 <= nx < N and 0 <= ny < N and examiner[nx][ny] == 0:
                examiner[nx][ny] = virus
                queue.append((virus, nx, ny, time + 1))


N, K = map(int, input().split())
examiner = [list(map(int, input().split())) for i in range(N)]
S, X, Y = map(int, input().split())

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque()
virus = [[] for i in range(K)]

for i in range(N):
    for j in range(N):
        if examiner[i][j] != 0:
            virus[examiner[i][j] - 1].append((examiner[i][j], i, j, 0))

for i in virus:
    for j in i:
        queue.append(j)

bfs()

print(examiner[X - 1][Y - 1])
