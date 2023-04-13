# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
count = 0

def add123(n, temp):
    global count
    if temp == n:
        count += 1
        return
    elif temp > n:
        return
    
    for i in range(1, 4):
        temp += i
        add123(n, temp)
        temp -= i
        
for i in arr:
    count = 0
    add123(i, 0)
    print(count)