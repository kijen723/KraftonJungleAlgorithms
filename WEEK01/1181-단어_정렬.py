# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

N = int(input())
word = []

for i in range(N):
    word.append(input())
    
word = set(word)
word = list(word)

word.sort()
word.sort(key=len)

for i in word:
    print(i, end='')