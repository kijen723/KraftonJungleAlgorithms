# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

formula = input().rstrip().split('-')
count = 0
for i in formula[0].split('+'):
    count += int(i)
for i in formula[1:]:
    for j in i.split('+'):
        count -= int(j)
print(count)