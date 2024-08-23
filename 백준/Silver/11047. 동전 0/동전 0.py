n, k = map(int,input().split())

arr = []
for _ in range (n):
    arr.append(int(input()))
arr.sort(reverse=True)
answer, b = 0,0
i=0
while k>0:
    answer += k // arr[i]
    b = k % arr[i]
    k = b
    i += 1
print(answer)