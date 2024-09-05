import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
visited = [[0]*N for _ in range(N)]
arr = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x, y):
    color = arr[x][y]
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<N:
            if visited[nx][ny] == 0 and arr[nx][ny] == color:
                dfs(nx, ny)

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt, end=' ')
cnt = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt)
