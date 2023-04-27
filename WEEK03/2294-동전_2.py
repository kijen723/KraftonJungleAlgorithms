# https://www.acmicpc.net/problem/2294

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        coin, count = queue.popleft()
        if coin == k:
            return count

        for i in coins:
            if i + coin <= k and check[i + coin] == 0:
                check[i + coin] = 1
                queue.append([i + coin, count + 1])
    
    return -1


n, k = map(int, input().split())
coins = set(int(input()) for i in range(n))
check = [0] * (k + 1)
queue = deque()
for i in coins:
    if i <= k:
        queue.append([i, 1])
        check[i] = 1

print(bfs())
