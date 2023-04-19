# https://www.acmicpc.net/problem/10830

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]


def matrix_square(matrix, matrix2):
    new_matrix = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_matrix[i][j] += matrix[i][k] * matrix2[k][j]
            new_matrix[i][j] %= 1000
    return new_matrix


def matrix_multi(A, B):
    if B == 1:
        return A
    else:
        square = matrix_multi(A, B // 2)
        if B % 2 == 0:
            return matrix_square(square, square)
        else:
            return matrix_square(matrix_square(square, square), A)


result = matrix_multi(A, B)

for i in result:
    for j in i:
        print(j % 1000, end=' ')
    print()
