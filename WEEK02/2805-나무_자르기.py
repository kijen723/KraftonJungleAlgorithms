# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for i in arr:
            if i - mid > 0:
                total += i - mid

        if target <= total:
            start = mid + 1
        else:
            end = mid - 1

    return end


print(binary_search(0, max(arr), M))
