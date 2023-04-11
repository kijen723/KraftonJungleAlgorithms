# https://www.acmicpc.net/problem/1065

import sys
input = sys.stdin.readline

N = int(input())
answer = 0

if N < 100:
    answer = N
else:
    answer += 99
    for i in range(100, N + 1):
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            answer += 1
                
print(answer)