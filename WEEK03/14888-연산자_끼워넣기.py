# https://www.acmicpc.net/problem/14888

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(depth, total, numadd, numsub, nummul, numdiv):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if numadd:
        dfs(depth + 1, total + A[depth], numadd - 1, numsub, nummul, numdiv)
    if numsub:
        dfs(depth + 1, total - A[depth], numadd, numsub - 1, nummul, numdiv)
    if nummul:
        dfs(depth + 1, total * A[depth], numadd, numsub, nummul - 1, numdiv)
    if numdiv:
        dfs(depth + 1, int(total / A[depth]), numadd, numsub, nummul, numdiv - 1)


N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

maximum = -sys.maxsize
minimum = sys.maxsize

dfs(1, A[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)
