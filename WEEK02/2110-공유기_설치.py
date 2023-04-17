# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = sorted([int(input()) for i in range(N)])


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        count = 1
        position = arr[0]

        for i in range(1, N):
            if arr[i] >= position + mid:
                count += 1
                position = arr[i]

        if target <= count:
            start = mid + 1
        else:
            end = mid - 1

    return end


print(binary_search(1, arr[-1] - arr[0], C))
