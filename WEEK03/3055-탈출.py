# https://www.acmicpc.net/problem/3055

from collections import deque
import sys
input = sys.stdin.readline


def bfs(Dx, Dy):
    while queue:
        x, y = queue.popleft()
        if map[Dx][Dy] == 'S':
            return visited[Dx][Dy]
        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if 0 <= nx < R and 0 <= ny < C:
                if (map[nx][ny] == '.' or map[nx][ny] == 'D') and map[x][y] == 'S':
                    map[nx][ny] = 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif (map[nx][ny] == '.' or map[nx][ny] == 'S') and map[x][y] == '*':
                    map[nx][ny] = '*'
                    queue.append((nx, ny))
    return "KAKTUS"


R, C = map(int, input().split())
map = [list(input().strip()) for i in range(R)]
visited = [[0] * C for i in range(R)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
queue = deque()

for i in range(R):
    for j in range(C):
        if map[i][j] == 'S':
            queue.append((i, j))
        elif map[i][j] == 'D':
            Dx, Dy = i, j

for i in range(R):
    for j in range(C):
        if map[i][j] == '*':
            queue.append((i, j))

print(bfs(Dx, Dy))