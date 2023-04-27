# https://www.acmicpc.net/problem/1388

import sys
input = sys.stdin.readline


def dfs(x, y):
    visited[x][y] = True

    if wood[x][y] == '-':
        for i in range(2):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and wood[nx][ny] == wood[x][y]:
                    dfs(nx, ny)

    else:
        for i in range(2, 4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and wood[nx][ny] == wood[x][y]:
                    dfs(nx, ny)


N, M = map(int, input().split())
wood = [list(input().strip()) for i in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[False] * (M) for i in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)
