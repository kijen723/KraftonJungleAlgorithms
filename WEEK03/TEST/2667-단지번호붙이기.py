# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    
    for i in range(4):
        nx = x + directions[i][0]
        ny = y + directions[i][1]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            dfs(nx, ny)
            
    

N = int(input())
house = [list(input().strip()) for i in range(N)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[False] * (N) for i in range(N)]
for i in range(N):
    for j in range(N):
        if house[i][j] == '0':
            visited[i][j] = True

answer = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count = 0
            dfs(i, j)
            answer.append(count)
            
answer.sort()

print(len(answer))
for i in answer:
    print(i)