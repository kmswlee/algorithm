n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
res = 1
max_len = max(n,m)
for i in range(n):
    for j in range(m):
        for k in range(1,max_len):
            if i+k > n-1 or j+k > m-1:
                continue
            if arr[i][j] != arr[i][j+k] or arr[i][j] != arr[i+k][j] or arr[i][j] != arr[i+k][j+k]:
                continue
            if arr[i][j] == arr[i][j+k] and arr[i][j] == arr[i+k][j] and arr[i][j] == arr[i+k][j+k]:
                res = max(res,(k+1)**2)
print(res)