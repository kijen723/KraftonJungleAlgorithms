# https://www.acmicpc.net/problem/7569

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = directions[i][0] + x
            ny = directions[i][1] + y
            nz = directions[i][2] + z

            if not 0 <= nx < H or not 0 <= ny < N or not 0 <= nz < M:
                continue

            if tomato[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx, ny, nz))
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                visited[nx][ny][nz] = True


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for i in range(N)] for i in range(H)]

queue = deque()
directions = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
visited = [[[False] * M for i in range(N)] for i in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))
                visited[i][j][k] = True

bfs()
answer = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))
print(answer - 1)
