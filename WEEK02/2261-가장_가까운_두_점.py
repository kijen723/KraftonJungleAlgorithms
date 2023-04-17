# https://www.acmicpc.net/problem/2261

import sys
input = sys.stdin.readline

N = int(input())
A = sorted([list(map(int, input().split())) for i in range(N)])


def distance(a, b):
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)


def near(start, end):
    if end - start == 1:
        return distance(A[start], A[end])

    mid = (start + end) // 2
    answer = min(near(start, mid), near(mid, end))
    target = []
    for i in range(start, end + 1):
        if (A[mid][0] - A[i][0]) ** 2 < answer:
            target.append(A[i])

    target.sort(key=lambda x: x[1])

    for i in range(len(target) - 1):
        for j in range(i + 1, len(target)):
            if (target[i][1] - target[j][1]) ** 2 < answer:
                answer = min(answer, distance(target[i], target[j]))
            else:
                break

    return answer


print(near(0, N - 1))
