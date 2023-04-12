# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i, j = 0, 0
    temparr = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temparr.append(left[i])
            i += 1
        else:
            temparr.append(right[j])
            j += 1
            
    temparr += left[i:]
    temparr += right[j:]
    
    return temparr

arr = merge_sort(arr)
for i in arr:
    print(i)