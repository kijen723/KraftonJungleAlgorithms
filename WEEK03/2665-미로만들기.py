# https://www.acmicpc.net/problem/2665

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[-1] * n for i in range(n)]
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            return visited[x][y]
        for i in range(4):
            nx = directions[i][0] + x
            ny = directions[i][1] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if maze[nx][ny] == 1:
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


n = int(input())
maze = [list(map(int, input().strip())) for i in range(n)]

directions = [[0, 1],[1, 0],[0, -1],[-1, 0]]

answer = bfs()

print(answer)