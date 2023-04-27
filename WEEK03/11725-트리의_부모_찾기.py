# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start):
    for i in graph[start]:
        if check[i] == 0:
            check[i] = start
            dfs(i)


N = int(input())
graph = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0] * (N + 1)

dfs(1)

for i in range(2, N + 1):
    print(check[i])


# from collections import deque
# import sys
# input = sys.stdin.readline


# def bfs():
#     while queue:
#         num = queue.popleft()
#         for i in graph[num]:
#             if check[i] == 0:
#                 check[i] = num
#                 queue.append(i)


# N = int(input())
# graph = [[] for i in range(N + 1)]
# for i in range(N - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# queue = deque([1])
# check = [0] * (N + 1)

# bfs()

# for i in range(2, N + 1):
#     print(check[i])
