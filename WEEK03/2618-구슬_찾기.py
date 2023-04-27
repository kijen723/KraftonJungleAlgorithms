# https://www.acmicpc.net/problem/2617

import sys
input = sys.stdin.readline


def dfs(graph, start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i)


N, M = map(int, input().split())
light = [[] for i in range(N + 1)]
heave = [[] for i in range(N + 1)]
for i in range(M):
    start, end = map(int, input().split())
    light[start].append(end)
    heave[end].append(start)

answer = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(light, i)
    if sum(visited) - 1 > N // 2:
        answer += 1
    else:
        visited = [0] * (N + 1)
        dfs(heave, i)
        if sum(visited) - 1 > N // 2:
            answer += 1
            
print(answer)
