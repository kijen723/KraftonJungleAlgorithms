# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    new = sorted([list(map(int, input().split())) for i in range(N)])
    
    temp, answer = 0, 1
    for i in range(1, len(new)):
        if new[i][1] < new[temp][1]:
            temp = i
            answer += 1
            
    print(answer)