import sys
sys.setrecursionlimit(10000)
def dfs(x,y):
    if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0:
        return
    grid[x][y] = 0 
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x-1,y-1)
    dfs(x-1,y+1)
    dfs(x+1,y-1)
    dfs(x+1,y+1)

while True:
    col, row  = map(int,input().split())
    if row+col == 0:
        break
    res = 0
    grid = [list(map(int,input().split())) for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                dfs(i,j)
                res+=1
    print(res)