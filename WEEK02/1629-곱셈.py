# https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())


def multi(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (multi(A, B // 2, C) ** 2) % C
    else:
        return ((multi(A, B // 2, C) ** 2) * A) % C


print(multi(A, B, C))
