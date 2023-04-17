# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    command = input()
    if 'push' in command:
        stack.append(int(command[5:]))
    elif 'pop' in command:
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif 'top' in command:
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])
