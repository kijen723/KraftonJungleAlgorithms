# https://www.acmicpc.net/problem/8958
 
import sys
input = sys.stdin.readline

case = int(input())
for i in range(case):
    count, score = 0, 0
    answer = input()
    for j in range(len(answer)):
        if answer[j] == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)