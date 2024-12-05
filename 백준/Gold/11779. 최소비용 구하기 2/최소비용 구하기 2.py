import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
d = [INF] * (n+1)

while(m) :
    m -= 1
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())
d[start] = 0
pre = [start] * (n+1)

q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if d[now] < dist:
        continue
    for i in graph[now]:
        nxt = dist + i[1]
        if nxt < d[i[0]]:
            d[i[0]] = nxt
            pre[i[0]] = now
            heapq.heappush(q,(nxt, i[0]))

print(d[end])   
city = []
cur = end
while cur!=start:
    city.append(cur)
    cur = pre[cur]
city.append(start)
city.reverse()
print(len(city))
print(*city)