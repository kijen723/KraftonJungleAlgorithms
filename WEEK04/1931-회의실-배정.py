# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for i in range(N)]
times.sort(key = lambda x : (x[1], x[0]))

count = 0
end = 0
for i in times:
    if i[0] >= end:
        count += 1
        end = i[1]
        
print(count)