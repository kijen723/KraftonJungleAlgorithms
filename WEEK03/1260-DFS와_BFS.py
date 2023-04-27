# https://www.acmicpc.net/problem/1260

from collections import deque
import sys
input = sys.stdin.readline


def dfs(start):
    checkDFS[start] = True
    routeDFS.append(start)
    for i in range(1, N + 1):
        if not checkDFS[i] and graph[start][i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    checkBFS[start] = True
    while queue:
        start = queue.popleft()
        routeBFS.append(start)
        for i in range(1, N + 1):
            if not checkBFS[i] and graph[start][i]:
                queue.append(i)
                checkBFS[i] = True


N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

checkDFS = [False] * (N + 1)
routeDFS = []
checkBFS = [False] * (N + 1)
routeBFS = []

dfs(V)
bfs(V)
print(*routeDFS)
print(*routeBFS)
