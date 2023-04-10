# https://www.acmicpc.net/problem/2562

import sys
input = sys.stdin.readline

# arr = []
# maxarr = 0
# indexmax = 0
# for i in range(9):
#     arr.append(int(input()))
#     if maxarr < arr[i]:
#         maxarr = arr[i]
#         indexarr = i + 1
# print(maxarr)
# print(indexarr)

arr = []
for i in range(9):
    arr.append(int(input()))
print(max(arr))
print(arr.index(max(arr))+1)