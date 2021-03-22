n = int(input())
arr = list(map(int,input().split()))
res=[]
for i in range(n):
    res.insert(arr[n-1-i],n-i)
print(*res)