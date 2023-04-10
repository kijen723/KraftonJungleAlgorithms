# https://www.acmicpc.net/problem/2675

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    answer = ''
    R, S = input().split()
    for j in S:
        answer += j * int(R)
    print(answer)