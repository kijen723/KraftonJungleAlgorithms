# https://www.acmicpc.net/problem/2470

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))


def binary_search(start, end):
    mix = arr[start] + arr[end]
    a, b = arr[start], arr[end]

    while start < end:
        newmix = arr[start] + arr[end]

        if abs(newmix) < abs(mix):
            mix = newmix
            a, b = arr[start], arr[end]

        if newmix < 0:
            start += 1
        elif newmix > 0:
            end -= 1
        else:
            return a, b

    return a, b


a, b = binary_search(0, N - 1)

print(a, b)
