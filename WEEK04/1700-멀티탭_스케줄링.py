# https://www.acmicpc.net/problem/1700

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
used = list(map(int, input().split()))

power_strip = [0] * N
count = 0
num = -1

for i in used:
    target = 0
    target_index = 0
    num += 1

    if i in power_strip:
        continue
    elif 0 in power_strip:
        power_strip[power_strip.index(0)] = i
    else:
        for j in power_strip:
            if j not in used[num:]:
                target = j
                break
            elif used[num:].index(j) > target_index:
                target_index = used[num:].index(j)
                target = j

        power_strip[power_strip.index(target)] = i
        count += 1

print(count)
