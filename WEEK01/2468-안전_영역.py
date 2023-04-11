# https://www.acmicpc.net/problem/2468

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

def solve(N):
    result = 0
    arr = [list(map(int, input().split())) for i in range(N)]

    def checkarea(x, y):
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        queue.append([x, y])
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in direction:
                px = x + dx
                py = y + dy
                
                if 0 <= px < N and 0 <= py < N and check[px][py] == 0:
                    check[px][py] += 1
                    queue.append([px, py])

    for h in range(101):
        count = 0
        check = [[0] * N for i in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] <= h:
                    check[i][j] = 1
                    
        for i in range(N):
            for j in range(N):
                if check[i][j] == 0:
                    check[i][j] += 1
                    checkarea(i, j)
                    count += 1
                    
        if count == 0:
            break
        
        result = max(result, count)
        
    return result
    
print(solve(N))