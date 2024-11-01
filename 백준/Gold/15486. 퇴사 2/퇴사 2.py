import sys
input = sys.stdin.readline

N = int(input())
t = [0 for _ in range(N)]
p = [0 for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    t[i], p[i] = map(int, input().split())

for i in range(N-1, -1, -1):
    if i + t[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + t[i]] + p[i])

print(dp[0])