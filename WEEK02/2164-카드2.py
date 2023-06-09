# https://www.acmicpc.net/problem/2164

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
