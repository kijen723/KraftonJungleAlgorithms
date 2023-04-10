# https://www.acmicpc.net/problem/2577

import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)
arr = [0] * 10

for i in range(10):
    for j in range(len(mul)):
        if str(i) == mul[j]:
            arr[i] += 1
    
for i in range(10):
    print(arr[i])