# https://www.acmicpc.net/problem/4344

import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    arr = list(map(int, input().split()))
    average = sum(arr[1:]) / arr[0]
    count = 0
    for i in arr[1:]:
        if i > average:
            count += 1
    print(f'{count / arr[0] * 100:.3f}%')