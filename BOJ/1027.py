from sys import stdin
n=int(stdin.readline().rstrip())
arr=list(map(int,stdin.readline().split()))
cnt=[0]*n
for i in range(n):
    max_heigh=float('-inf')
    for j in range(i+1,n):
        now_heigh=(arr[j]-arr[i])/(j-i)
        if now_heigh > max_heigh:
            cnt[j]+=1
            cnt[i]+=1
            max_heigh=now_heigh
print(max(cnt))

