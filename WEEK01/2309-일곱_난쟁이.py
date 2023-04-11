# https://www.acmicpc.net/problem/2309

import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
    
for i in range(8):
    for j in range(i + 1, 9):
        temparr = arr[:]
        temparr[i], temparr[j] = 0, 0
        if sum(temparr) == 100:
            break
    if sum(temparr) == 100:
        break
            
for i in temparr:
    if i != 0:
        print(i)