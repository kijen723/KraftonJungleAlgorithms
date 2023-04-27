# https://www.acmicpc.net/problem/21606

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(point, count):
    check[point] = True
    for i in graph[point]:
        if A[i] == 1:
            count += 1
        elif not check[i] and A[i] == 0:
            count = dfs(i, count)
    return count


N = int(input())
A = [0] + list(map(int, input().strip()))
graph = [[] for i in range(N + 1)]
answer = 0
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if A[a] == 1 and A[b] == 1:
        answer += 2

sum = 0
check = [0] * (N + 1)

for i in range(1, N + 1):
    if not check[i] and A[i] == 0:
        x = dfs(i, 0)
        sum += x * (x - 1)

print(answer + sum)
