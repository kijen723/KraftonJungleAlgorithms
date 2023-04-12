# https://www.acmicpc.net/problem/10819

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

temparr = []
check = [0] * N
answer = 0

def permutation():
    global check, answer
    if len(temparr) == N:
        total_sum = 0
        for i in range(N - 1):
            total_sum += abs(temparr[i] - temparr[i + 1])
        answer = max(answer, total_sum)
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            temparr.append(arr[i])
            permutation()
            temparr.pop()
            check[i] = 0

permutation()

print(answer)