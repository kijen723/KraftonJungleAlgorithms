# https://www.acmicpc.net/problem/2628

import sys
input = sys.stdin.readline

answer = 0
width, height = map(int, input().split())
count = int(sys.stdin.readline())
indexwidth, indexheight = [0, width], [0, height]
for i in range(count):
    cut, index = map(int, input().split())
    if cut == 1:
        indexwidth.append(index)
    else:
        indexheight.append(index)
indexwidth.sort()
indexheight.sort()

for i in range(1, len(indexwidth)):
    for j in range(1, len(indexheight)):
        answer = max(answer, (indexwidth[i] - indexwidth[i - 1]) * (indexheight[j] - indexheight[j - 1]))
print(answer)