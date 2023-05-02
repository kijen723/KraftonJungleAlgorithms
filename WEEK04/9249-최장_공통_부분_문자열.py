# https://www.acmicpc.net/problem/9249

import sys
input = sys.stdin.readline


def get_suffix():
    suffix = [i for i in range(lenSUM)]
    grade = [0] * (lenSUM+1)
    new_grade = [0] * (lenSUM + 1)

    for i in range(lenSUM):
        grade[i] = ord(sumAB[i])

    grade[lenSUM] = -1
    new_grade[lenSUM] = -1

    t = 1
    while t < lenSUM:
        suffix.sort(key=lambda x: (grade[x], grade[min(x + t, lenSUM)]))

        for i in range(1, lenSUM):
            p, q = suffix[i-1], suffix[i]

            if grade[p] != grade[q] or grade[min(p + t, lenSUM)] != grade[min(q + t, lenSUM)]:
                new_grade[q] = new_grade[p] + 1
            else:
                new_grade[q] = new_grade[p]

        if new_grade[lenSUM - 1] == lenSUM-1:
            break

        t *= 2
        grade = new_grade[:]

    return suffix, grade


def get_LCP(suffix, grade):
    LCP = [0] * lenSUM
    length = 0
    for i in range(lenSUM):
        k = grade[i]
        if k == 0:
            continue
        p = suffix[k-1]

        while i + length < lenSUM and p + length < lenSUM and sumAB[i + length] == sumAB[p + length]:
            length += 1
        LCP[k] = length

        if length:
            length -= 1

    return LCP


def print_answer(suffix, LCP):
    target = (0, 0)
    for i, j in enumerate(LCP):
        if 0 <= suffix[i - 1] + j - 1 < len(A) and len(A) < suffix[i] + j - 1 < lenSUM:
            target = max(target, (j, i))
        if 0 <= suffix[i] + j - 1 < len(A) and len(A) < suffix[i-1] + j - 1 < lenSUM:
            target = max(target, (j, i))

    length, start = target
    print(length)
    print(sumAB[suffix[start]: suffix[start] + length])


A = input().rstrip()
B = input().rstrip()
sumAB = A + '1' + B
lenSUM = len(sumAB)

suffix, grade = get_suffix()
LCP = get_LCP(suffix, grade)
print_answer(suffix, LCP)