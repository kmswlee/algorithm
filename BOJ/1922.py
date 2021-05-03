import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = [i for i in range(N+1)]
def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]
def union(x,y):
    x,y = find(x),find(y)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y
res = 0
link = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    link.append([a,b,cost])
for a,b,cost in sorted(link,key = lambda x:x[2]):
    if not (find(a) == find(b)):
        union(a,b)
        res+=cost
print(res)