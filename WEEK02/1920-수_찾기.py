# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

N = int(input())
Narr = sorted(list(map(int, input().split())))
M = int(input())
Marr = list(map(int, input().split()))


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if target > Narr[mid]:
            start = mid + 1
        elif target < Narr[mid]:
            end = mid - 1
        else:
            return 1
    return 0


for i in Marr:
    print(binary_search(0, N - 1, i))
