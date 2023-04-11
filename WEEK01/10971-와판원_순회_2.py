# https://www.acmicpc.net/problem/10971

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
price = []
for i in range(N):
    price.append(list(map(int, input().split())))

def main(N, price):
    answer = sys.maxsize
    arr = [i for i in range(N)]
    permuarr = list(permutations(arr, N))
    
    for i in permuarr:
        totalsum = 0
        possible = True
        
        for j in range(N - 1):
            if price[i[j]][i[j + 1]] != 0:
                totalsum += price[i[j]][i[j + 1]]
            else:
                possible = False
                break
            
        if price[i[-1]][i[0]] != 0:
            totalsum += price[i[-1]][i[0]]
        else:
            possible = False

        if possible == True:
            answer = min(answer, totalsum)
            
    return answer

print(main(N, price))