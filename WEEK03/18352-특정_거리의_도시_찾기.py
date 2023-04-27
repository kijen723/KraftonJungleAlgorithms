# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visitied[start] = True
    while queue:
        city = queue.popleft()
        for i in route[city]:
            if not visitied[i]:
                visitied[i] = True
                distance[i] = distance[city] + 1
                queue.append(i)
                if distance[i] == K:
                    answer.append(i)


N, M, K, X = map(int, input().split())
route = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    route[A].append(B)

visitied = [False] * (N + 1)
distance = [0] * (N + 1)
answer = []

bfs(X)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
