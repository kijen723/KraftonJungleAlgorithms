# https://www.acmicpc.net/problem/2588

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

print(a * ((b % 10)))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)