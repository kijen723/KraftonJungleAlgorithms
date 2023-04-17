# https://www.acmicpc.net/problem/3190

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * N for i in range(N)]
K = int(input())
for i in range(K):
    apple = list(map(int, input().split()))
    board[apple[0] - 1][apple[1] - 1] = 2
L = int(input())
turntimes = deque([list(map(str, input().split())) for i in range(L)])

queue = deque([[0, 0]])
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
x, y, direction, time = 0, 0, 0, 0

while True:
    time += 1
    x += directions[direction][0]
    y += directions[direction][1]

    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        break

    if board[x][y] == 2:
        board[x][y] = 1
        queue.append([x, y])
    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append([x, y])
        tail = queue.popleft()
        board[tail[0]][tail[1]] = 0
    else:
        break

    if turntimes:
        if str(time) == turntimes[0][0]:
            if turntimes[0][1] == 'L':
                direction = (direction - 1) % 4
                turntimes.popleft()
            else:
                direction = (direction + 1) % 4
                turntimes.popleft()

print(time)
