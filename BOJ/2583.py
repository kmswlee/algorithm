import sys
sys.setrecursionlimit(10000)
r,c,k = map(int,input().split())
g = [[0]*c for _ in range(r)]
for _ in range(k):
    x1,y1,x2,y2  = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            g[i][j] = 1
def dfs(x,y):
    if x < 0 or x >= r or y < 0 or y >= c or g[x][y]:
        return 0
    g[x][y] = 1
    return 1+dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)
res = []
for i in range(r):
    for j in range(c):
        if g[i][j] == 0:
            res.append(dfs(i,j))
print(len(res))
print(*sorted(res))
