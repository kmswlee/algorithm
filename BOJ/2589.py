import collections,sys
row, col = map(int,input().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(row)]
q = collections.deque()
def bfs(x,y):
    q.append([x,y])
    grid = [[-1]*col for _ in range(row)]
    grid[x][y] = 0
    while q:
        x,y = q.popleft()
        if x > 0 and grid[x-1][y] == -1 and board[x-1][y] == "L":
            grid[x-1][y] = grid[x][y] + 1
            q.append((x-1,y))
        if y > 0 and grid[x][y-1] == -1 and board[x][y-1] == "L":
            grid[x][y-1] = grid[x][y] + 1
            q.append((x,y-1))
        if x < row-1 and grid[x+1][y] == -1 and board[x+1][y] == "L":
            grid[x+1][y] = grid[x][y] + 1
            q.append((x+1,y))
        if y < col-1 and grid[x][y+1] == -1 and board[x][y+1] == "L":
            grid[x][y+1] = grid[x][y] + 1
            q.append((x,y+1))
    return grid[x][y]
res = 0
for i in range(row):
    for j in range(col):
        if board[i][j] == 'L':
            res = max(res,bfs(i,j))
print(res)