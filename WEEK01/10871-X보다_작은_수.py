# https://www.acmicpc.net/problem/10871

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, (input().split())))
for i in range(N):
    if A[i] < X:
        print(A[i])