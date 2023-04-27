# https://www.acmicpc.net/problem/1707

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start, group):
    check[start] = group

    for i in graph[start]:
        if not check[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif check[i] == check[start]:
            return False

    return True


K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    check = [0] * (V + 1)

    for i in range(1, V + 1):
        if not check[i]:
            answer = dfs(i, 1)
            if not answer:
                break

    print("YES" if answer else "NO")


# import sys
# from collections import deque
# input = sys.stdin.readline


# def bfs(start, group):
#     queue = deque([start])
#     check[start] = group

#     while queue:
#         x = queue.popleft()

#         for i in graph[x]:
#             if not check[i]:
#                 queue.append(i)
#                 check[i] = -check[x]
#             elif check[i] == check[x]:
#                 return False

#     return True


# K = int(input())
# for i in range(K):
#     V, E = map(int, input().split())
#     graph = [[] for i in range(V + 1)]
#     for i in range(E):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     check = [0] * (V + 1)

#     for i in range(1, V + 1):
#         if not check[i]:
#             answer = bfs(i, 1)
#             if not answer:
#                 break

#     print("YES" if answer else "NO")
