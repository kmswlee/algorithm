L, N =map(int,input().split())
arr = sorted(input().split())
dic = {'a','e','i','o','u'}
def dfs(num,arr,vowels_cnt):
    if L == len(num) and 1 <= vowels_cnt <= L-2:
        print(num)
        return
    for i,v in enumerate(arr):
        if v in dic:    
            dfs(num+v,arr[i+1:],vowels_cnt+1)
        else:
            dfs(num+v,arr[i+1:],vowels_cnt)

for i,v in enumerate(arr):
    res = v
    if v in dic:
        dfs(res,arr[i+1:],1)
    else:
        dfs(res,arr[i+1:],0)