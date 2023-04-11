# https://www.acmicpc.net/problem/2869

import sys
input = sys.stdin.readline
import math

A, B, V = map(int, input().split())
answer = math.ceil((V - B) / (A - B))
print(answer)

# answer = (V - B) / (A - B)
# if answer - int(answer) != 0:
#     answer += 1
# print(int(answer))