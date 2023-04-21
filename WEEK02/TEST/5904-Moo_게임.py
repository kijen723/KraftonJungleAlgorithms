# https://www.acmicpc.net/problem/5904

import sys
input = sys.stdin.readline


def checkindex(len, mid, target):
    left = (len - mid) // 2
    if target <= left:
        return checkindex(left, mid - 1, target)
    elif left < target <= left + mid:
        if target - left - 1 == 0:
            return 'm'
        else:
            return 'o'
    else:
        return checkindex(left, mid - 1, target - left - mid)


N = int(input())

len, n = 3, 0

while N > len:
    n += 1
    len = (len * 2) + (n + 3)

print(checkindex(len, n + 3, N))
