# https://www.acmicpc.net/problem/10872

import sys
input = sys.stdin.readline

n = int(input())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(n))