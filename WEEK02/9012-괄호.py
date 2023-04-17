# https://www.acmicpc.net/source/59406779

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    VPS = input().rstrip()
    stack = []
    check = True

    for j in VPS:
        if j == '(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                check = False
                break

    if check and not stack:
        print("YES")
    else:
        print('NO')
