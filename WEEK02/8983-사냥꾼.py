# https://www.acmicpc.net/problem/8983

import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
shoot = sorted(list(map(int, input().split())))
animal = [list(map(int, input().split())) for i in range(N)]


def binary_search():
    count = 0
    for a, b in animal:
        start, end = 0, M - 1

        while start <= end:
            mid = (start + end) // 2
            if abs(shoot[mid] - a) + b <= L:
                count += 1
                break

            if shoot[mid] < a:
                start = mid + 1
            else:
                end = mid - 1

    return count


print(binary_search())
