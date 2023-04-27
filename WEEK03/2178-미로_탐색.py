# https://www.acmicpc.net/problem/2178

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = directions[i][0] + x
            ny = directions[i][1] + y
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
            if nx == N and ny == M:
                break


N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for i in range(N)]

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

bfs()

print(maze[N - 1][M - 1])
