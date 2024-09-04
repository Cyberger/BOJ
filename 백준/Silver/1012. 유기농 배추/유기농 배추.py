T = int(input())

for _ in range(T):
    M, N, K = map(int,input().split())
    arr = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int,input().split())
        arr[x][y] = 1

    def dfs(x, y):
        if x < 0 or x >= M or y < 0 or y >= N:
            return False
        if arr[x][y] == 1:
            arr[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False
    
    result = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                result += 1

    print (result)