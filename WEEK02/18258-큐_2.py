# https://www.acmicpc.net/problem/18258

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque()

for i in range(N):
    command = input().rstrip()

    if 'push' in command:
        queue.append(command[5:])
    elif 'pop' in command:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in command:
        if queue:
            print(queue[-1])
        else:
            print(-1)
