# https://www.acmicpc.net/problem/2606

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        point = queue.popleft()
        check[point] = 1
        for i in graph[point]:
            if check[i] == 0:
                queue.append(i)
                check[i] = 1


N = int(input())
M = int(input())
graph = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
check = [0] * (N + 1)

queue = deque([1])
bfs()
print(sum(check) - 1)



# from collections import deque
# import sys
# input = sys.stdin.readline


# def bfs():
#     while queue:
#         point = queue.popleft()
#         check[point] = 1
#         for i in graph[point]:
#             if check[i] == 0:
#                 queue.append(i)
#                 check[i] = 1


# N = int(input())
# M = int(input())
# graph = [[] for i in range(N + 1)]

# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# check = [0] * (N + 1)

# queue = deque([1])
# bfs()
# print(sum(check) - 1)
