# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
    
for i in range(N - 1):
    for j in range(i, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)