# https://www.acmicpc.net/problem/11866

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])
answer = []

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end='')

for i in answer:
    if i != answer[-1]:
        print(i, end=', ')
    else:
        print(i, end='')

print(">")
