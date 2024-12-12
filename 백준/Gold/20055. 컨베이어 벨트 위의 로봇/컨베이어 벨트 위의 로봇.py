import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))

robot = deque([0]*N)
answer = 0

while True:
    answer += 1
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and A[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            A[i+1] -= 1

    if robot[-1] == 1:
        robot[-1] = 0

    if A[0] > 0:
        robot[0] = 1
        A[0] -= 1

    if A.count(0) >= K:
        break
    
print(answer)