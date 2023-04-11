# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

n = int(input())
row = [0] * n
answer = 0

def check(a):
    for i in range(a):
        if row[a] == row[i] or abs(row[a] - row[i]) == abs(a - i):
            return False
    return True
    
def queen(a):
    global answer
    if a == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[a] = i
            if check(a):
                queen(a + 1)
        
queen(0)
print(answer)