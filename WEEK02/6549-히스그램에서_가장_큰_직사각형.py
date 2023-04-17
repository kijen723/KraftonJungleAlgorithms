# https://www.acmicpc.net/problem/6549

import sys
input = sys.stdin.readline


def max_area(heights):
    if len(heights) == 1:
        return heights[0]

    mid = len(heights) // 2
    left, right = mid - 1, mid
    height = min(heights[left], heights[right])
    width = 2
    area = height * width

    left_area = max_area(heights[:mid])
    right_area = max_area(heights[mid:])

    while left > 0 or right < len(heights) - 1:
        if left == 0:
            right += 1
            next_height = heights[right]
        elif right == len(heights) - 1:
            left -= 1
            next_height = heights[left]
        elif heights[left - 1] > heights[right + 1]:
            left -= 1
            next_height = heights[left]
        else:
            right += 1
            next_height = heights[right]

        height = min(height, next_height)
        width += 1
        area = max(area, height * width)

    return max(area, left_area, right_area)


while True:
    heights = list(map(int, input().split()))
    if heights[0] == 0:
        break
    print(max_area(heights[1:]))
