N = int(input())
arr=[]
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))
end = arr[0][1]

count=1
for i in range(1, N):
    if arr[i][0] >= end:
        count+=1
        end = arr[i][1]
print(count)