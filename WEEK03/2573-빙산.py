# https://www.acmicpc.net/problem/2573

from collections import deque
import sys
input = sys.stdin.readline


def dfs(q, w):
    queue.append((q, w))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = directions[i][0] + x
            ny = directions[i][1] + y
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                visited[nx][ny] = False
                if iceberg[nx][ny] != 0:
                    queue.append((nx, ny))
                    


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for i in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * M for i in range(N)]
answer = 0
queue = deque()

while True:
    answer += 1
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0:
                visited[i][j] = True
                ice = iceberg[i][j]
                for k in range(4):
                    nx = directions[k][0] + i
                    ny = directions[k][1] + j
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if iceberg[nx][ny] == 0:
                            ice -= 1
                            if ice == 0:
                                break
                iceberg[i][j] = ice

    piece = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and visited[i][j]:
                dfs(i, j)
                piece += 1
            elif iceberg[i][j] == 0 and visited[i][j]:
                visited[i][j] = False

    if piece >= 2:
        print(answer)
        break
    elif piece == 0:
        print(0)
        break
