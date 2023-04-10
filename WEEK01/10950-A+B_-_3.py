# https://www.acmicpc.net/problem/10950

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A + B)