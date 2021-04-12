n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key = len)
res=0
for i in range(n):
    ch_head = False
    for j in range(i+1,n):
        if arr[j].startswith(arr[i]):
            ch_head = True
            break
    if not ch_head:
        res+=1
print(res)
