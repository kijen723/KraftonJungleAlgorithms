# https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline


def find(n):
    if n != root[n]:
        return find(root[n])
    return root[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        root[a] = root[b]
    else:
        root[b] = root[a]


V, E = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(E)]
graph.sort(key=lambda x: x[2])
root = [i for i in range(V + 1)]
answer = 0

for start, end, length in graph:
    if find(start) != find(end):
        union(start, end)
        answer += length

print(answer)


# import heapq
# import sys
# input = sys.stdin.readline


# def prim():
#     check = [False] * (V + 1)
#     queue = [[0, 1]]
#     answer = 0
#     count = 0
#     while count < V:
#         length, point = heapq.heappop(queue)
#         if not check[point]:
#             check[point] = True
#             answer += length
#             count += 1
#             for i in route[point]:
#                 heapq.heappush(queue, i)
#     return answer


# V, E = map(int, input().split())
# route = [[] for i in range(V + 1)]
# for i in range(E):
#     A, B, C = map(int, input().split())
#     route[A].append([C, B])
#     route[B].append([C, A])

# print(prim())
