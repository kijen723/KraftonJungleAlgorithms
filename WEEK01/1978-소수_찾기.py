# https://www.acmicpc.net/problem/1978

import sys
input = sys.stdin.readline

answer = 0
N = int(input())
arr = list(map(int, input().split()))

def prime(n):
    for i in range(n):
        if n == 1:
            return False
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                return False
        return True

for i in arr:
    if prime(i):
        answer += 1
        
print(answer)