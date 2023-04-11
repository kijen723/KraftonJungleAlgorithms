# https://www.acmicpc.net/problem/1914

import sys
input = sys.stdin.readline

n = int(input())

def hanoi(n, start, mid ,end):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n - 1, start, end, mid)
        print(start, end)
        hanoi(n - 1, mid, start, end)
        
print((2 ** n) - 1)

if n <= 20:
    hanoi(n, 1, 2, 3)