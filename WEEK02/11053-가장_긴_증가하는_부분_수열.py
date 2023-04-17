# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
subsequence = [arr[0]]


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if target > subsequence[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start


for i in range(1, N):
    if arr[i] > subsequence[-1]:
        subsequence.append(arr[i])
    else:
        index = binary_search(0, len(subsequence) - 1, arr[i])
        subsequence[index] = arr[i]

print(len(subsequence))
