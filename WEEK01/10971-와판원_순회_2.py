# https://www.acmicpc.net/problem/10971

import sys
input = sys.stdin.readline

N = int(input())
price = [list(map(int, input().split())) for i in range(N)]

answer = sys.maxsize
check = [0] * N

def travel(start, now, totalsum, count):
    global answer
    if count == N:
        if price[now][start]:
            totalsum += price[now][start]
            answer = min(answer, totalsum)
        return
    
    if totalsum > answer:
        return
    
    for i in range(N):
        if check[i] == 0 and price[now][i] != 0:
            check[i] = 1
            travel(start, i, totalsum + price[now][i], count + 1)
            check[i] = 0
            
for i in range(N):
    check[i] = 1
    travel(i, i, 0, 1)
    check[i] = 0

print(answer)