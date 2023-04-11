# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def solve(N, r, c):
    if N == 0:
        return 0
    return ((2 * (r % 2)) + (c % 2)) + (4 * solve(N - 1, int(r / 2), int(c / 2)))

print(solve(N, r, c))