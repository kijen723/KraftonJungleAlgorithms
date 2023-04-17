# https://www.acmicpc.net/problem/2812

import sys
input = sys.stdin.readline


def bigger():
    N, K = map(int, input().split())
    number = input().rstrip()
    length = N - K
    stack = []
    answer = ''

    for i in number:
        while stack and K > 0 and stack[-1] < i:
            stack.pop()
            K -= 1

        stack.append(i)

    for i in range(length):
        answer += stack[i]

    return answer


print(bigger())
