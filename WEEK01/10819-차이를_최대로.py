# https://www.acmicpc.net/problem/10819

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
permuarr = list(permutations(arr, N))

for i in permuarr:
    totalsum = 0
    for j in range(len(i) - 1):
        totalsum += abs(i[j] - i[j + 1])
    answer = max(answer, totalsum)
print(answer)