# https://www.acmicpc.net/problem/16120

import sys
input = sys.stdin.readline

string = input().rstrip()
ppap = ['P', 'P', 'A', 'P']
stack = []

for i in string:
    stack.append(i)

    if len(stack) >= 4 and stack[-4:] == ppap:
        for i in range(3):
            stack.pop()

if len(stack) == 1 and string[0] == 'P':
    print('PPAP')
else:
    print('NP')
