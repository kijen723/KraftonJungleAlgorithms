# https://www.acmicpc.net/problem/1110

import sys
input = sys.stdin.readline

N = int(input())
temp = N
one, ten, count = 0, 0, 0

while True:
    one = temp % 10
    ten = temp // 10
    temp = (one * 10) + ((one + ten) % 10) 
    count += 1
    if temp == N:
        break

print(count)

# N = input()

# if len(N) < 2:
#     N += "0"
#     N = N[::-1]
    
# if int(N[0]) + int(N[1]) < 10:
#     temp = N[1] + str(int(N[0]) + int(N[1:]))
# else:
#     temp = N[1] + str(int(N[0]) + int(N[1:]))[1:]
# count = 1

# while temp != N:
#     if int(temp[0]) + int(temp[1]) < 10:
#         temp = temp[1] + str(int(temp[0]) + int(temp[1]))
#     else:
#         temp = temp[1] + str(int(temp[0]) + int(temp[1]))[1]
#     count += 1

# print(count)