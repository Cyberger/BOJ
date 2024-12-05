import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
d = [INF] * (V+1)

while(E) :
    E -= 1
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

d[start] = 0
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
            heapq.heappush(q,(nxt, i[0]))

for i in range(1, V+1):
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])