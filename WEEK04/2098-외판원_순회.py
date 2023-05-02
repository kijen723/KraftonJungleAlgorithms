# https://www.acmicpc.net/problem/2098

import sys
input = sys.stdin.readline


def dfs(i, visited):
    if dp[i][visited] != 0:
        return dp[i][visited]

    if visited == (1 << (N - 1)) - 1:
        if fees[i][0]:
            return fees[i][0]
        else:
            return sys.maxsize

    min_distance = sys.maxsize
    for j in range(1, N):
        if not fees[i][j]:
            continue
        if visited & (1 << (j - 1)):
            continue
        min_distance = min(
            min_distance, fees[i][j] + dfs(j, visited | (1 << (j - 1))))
    dp[i][visited] = min_distance

    return min_distance


N = int(input())
fees = [list(map(int, input().split())) for i in range(N)]

dp = [[0] * (1 << (N - 1)) for i in range(N)]

print(dfs(0, 0))
