import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N,M = map(int,input().split())
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

for _ in range(M):
    ch,a,b  = map(int,input().split())
    if ch == 0:
        if not (find(a) == find(b)):
            union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")