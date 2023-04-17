# https://www.acmicpc.net/problem/11279

import sys
input = sys.stdin.readline


def insertheap(n):
    heap.append(n)
    index = len(heap) - 1

    while index > 0:
        parentindex = (index - 1) // 2
        if heap[index] > heap[parentindex]:
            heap[index], heap[parentindex] = heap[parentindex], heap[index]
            index = parentindex
        else:
            break


def deleteheap():
    if not heap:
        return 0

    heap[0], heap[-1] = heap[-1], heap[0]
    maxheap = heap.pop()
    index = 0

    while index < len(heap) - 1:
        leftindex, rightindex = (index * 2) + 1, (index * 2) + 2
        if rightindex < len(heap):
            if heap[leftindex] >= heap[rightindex] and heap[leftindex] >= heap[index]:
                heap[leftindex], heap[index] = heap[index], heap[leftindex]
                index = leftindex
            elif heap[rightindex] > heap[leftindex] and heap[rightindex] > heap[index]:
                heap[rightindex], heap[index] = heap[index], heap[rightindex]
                index = rightindex
            else:
                break
        elif leftindex < len(heap):
            if heap[leftindex] > heap[index]:
                heap[leftindex], heap[index] = heap[index], heap[leftindex]
                index = leftindex
            else:
                break
        else:
            break

    return maxheap


N = int(input())

heap = []

for i in range(N):
    num = int(input())

    if num == 0:
        print(deleteheap())
    else:
        insertheap(num)


# import heapq
# import sys
# input = sys.stdin.readline

# N = int(input())
# heap = []

# for i in range(N):
#     num = int(input())
#     if num != 0:
#         heapq.heappush(heap, -num)
#     else:
#         if heap:
#             print(-heapq.heappop(heap))
#         else:
#             print(0)
