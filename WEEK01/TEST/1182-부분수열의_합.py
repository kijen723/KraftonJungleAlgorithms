# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
temparr = []

def sumcombi(start):
    global count
    if sum(temparr) == S and len(temparr) != 0:
        count += 1
        
    for i in range(start, N):
        temparr.append(arr[i])
        sumcombi(i + 1)
        temparr.pop()
        
sumcombi(0)
print(count)