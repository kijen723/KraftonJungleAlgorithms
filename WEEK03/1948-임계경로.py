# https://www.acmicpc.net/problem/1948

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
route = [[] for i in range(n + 1)]
topology = [0] * (n + 1)
for i in range(m):
    a, b, t = map(int, input().split())
    route[a].append((b, t))
    topology[b] += 1
start, end = map(int, input().split())

times = [0] * (n + 1)
maxroad = [[] for i in range(n + 1)]
queue = deque([start])

while queue:
    city = queue.popleft()
    
    for next, time in route[city]:
        topology[next] -= 1
        
        if times[next] < times[city] + time:
            times[next] = times[city] + time
            maxroad[next] = [city]
        elif times[next] == times[city] + time:
            maxroad[next].append(city)
        
        if topology[next] == 0:
            queue.append(next)
            
queue.append(end)
road = set()

while queue:
    city = queue.popleft()
    
    for next in maxroad[city]:
        if (city, next) not in road:
            road.add((city, next))
            queue.append(next)
            
print(times[end])
print(len(road))