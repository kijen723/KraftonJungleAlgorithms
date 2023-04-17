# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
white, blue = 0, 0


def square(x, y, n):
    global white, blue
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:
                square(x, y, n // 2)
                square(x, y + (n // 2), n // 2)
                square(x + (n // 2), y, n // 2)
                square(x + (n // 2), y + (n // 2), n // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


square(0, 0, N)
print(white)
print(blue)
