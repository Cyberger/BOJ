import sys
input = sys.stdin.readline

N = int(input())
schedule = [0] * 366

for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        schedule[i] += 1

answer = 0
w = 0
h = 0
for i in range(1, 366):
    if schedule[i] != 0:
        w += 1
        h = max(h, schedule[i])
    else:
        answer += w*h
        w = 0
        h = 0
answer += w*h
print(answer)