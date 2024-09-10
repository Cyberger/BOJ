from collections import deque
M, N, H = map(int, input().split())

tmt = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

d = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
def bfs():
    global day
    while q:
        day += 1
        for _ in range(len(q)):
            x, y, z = q.popleft()
            for dx, dy, dz in d:
                nx, ny, nz = x+dx, y+dy, z+dz
                if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and tmt[nx][ny][nz] == 0:
                    tmt[nx][ny][nz] = 1
                    q.append((nx, ny, nz))


day = -1 
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tmt[i][j][k] == 1:
                q.append((i, j, k))

bfs()

for i in tmt:
    for j in i:
        for k in j:
            if k == 0:
                day=-1
                break

print(day)
