import sys
sys.setrecursionlimit(100000)
N = int(input())
def dfs(x,y):
        if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0:
            return 
        grid[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

while N:
    row, col, k = map(int, input().split())
    grid = [[0]*col for _ in range(row)]
    for i in range(k):
        x, y = map(int, input().split())
        grid[x][y] = 1
    res = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                dfs(i,j)
                res+=1
    print(res)
    N-=1
