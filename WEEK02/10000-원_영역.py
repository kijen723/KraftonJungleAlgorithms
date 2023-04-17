# https://www.acmicpc.net/problem/10000

import sys
input = sys.stdin.readline

N = int(input())

circles = []
for i in range(N):
    x, r = map(int, input().split())
    circles.append([x-r, '{', 0])
    circles.append([x+r, ')', 0])

circles.sort(key=lambda x: (x[0], x[1]))
stack = []
count = 1

for i in range(len(circles)):
    if circles[i][1] == "{":
        if stack and stack[-1][0] == circles[i][0]:
            stack[-1][2] = 1
            stack.append(circles[i])
        else:
            stack.append(circles[i])
    else:
        if stack[-1][2] == 1:
            count += 1
        count += 1
        stack.pop()
        if stack:
            if circles[i][0] != circles[i + 1][0]:
                stack[-1][2] = 0

print(count)
