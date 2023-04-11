# https://www.acmicpc.net/problem/9020

import sys
input = sys.stdin.readline

T = int(sys.stdin.readline())

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(T):
    num = int(input())
    left, right = int(num / 2), int(num / 2)
    while left > 0:
        if prime(left) and prime(right):
            print(left, right)
            break
        else:
            left -= 1
            right += 1