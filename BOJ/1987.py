row, col = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input())) for _ in range(row)]
path = [0]*26
res = 1
def dfs(x,y,cnt):
    global res
    res = max(res,cnt)
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        nx,ny = x + dx,y + dy
        if 0 <= nx < row and 0 <= ny < col and path[board[nx][ny]] == 0:
            path[board[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            path[board[nx][ny]] = 0

path[board[0][0]] = 1
dfs(0,0,1)
print(res)

# 시간초과