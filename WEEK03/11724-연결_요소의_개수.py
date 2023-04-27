# https://www.acmicpc.net/problem/11724

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    check[start] = True
    while queue:
        point = queue.popleft()
        for i in graph[point]:
            if not check[i]:
                check[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False] * (N + 1)
answer = 0

for i in range(1, N + 1):
    if not check[i]:
        if not graph[i]:
            answer += 1
            check[i] = True
        else:
            bfs(i)
            answer += 1

print(answer)
