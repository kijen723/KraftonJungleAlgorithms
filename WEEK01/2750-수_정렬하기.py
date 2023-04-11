# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
    
def quicksort(arr, left, right):
    templeft = left
    tempright = right
    pivot = arr[(left + right) // 2]
    
    while templeft <= tempright:
        while arr[templeft] < pivot:
            templeft += 1
        while arr[tempright] > pivot:
            tempright -= 1
        if templeft <= tempright:
            arr[templeft], arr[tempright] = arr[tempright], arr[templeft]
            templeft += 1
            tempright -= 1
        
    if left < tempright:
        quicksort(arr, left, tempright)
    if right > templeft:
        quicksort(arr, templeft, right)

quicksort(arr, 0, N - 1)

for i in arr:
    print(i)