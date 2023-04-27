# https://www.acmicpc.net/problem/1916

import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    heap = []
    expense[start] = 0
    heapq.heappush(heap, (expense[start], start))

    while heap:
        fee, goal = heapq.heappop(heap)

        if expense[goal] < fee:
            continue

        for next_goal, next_fee in route[goal]:
            next_expense = fee + next_fee

            if next_expense < expense[next_goal]:
                expense[next_goal] = next_expense
                heapq.heappush(heap, (expense[next_goal], next_goal))


N = int(input())
M = int(input())
route = [[] for i in range(N + 1)]
for i in range(M):
    A, B, C = map(int, input().split())
    route[A].append((B, C))
start, end = map(int, input().split())

expense = [sys.maxsize] * (N + 1)

dijkstra(start)
print(expense[end])
