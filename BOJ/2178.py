import collections
row,col = map(int,input().split())
board = []
for _ in range(row):
    board.append(list(input()))
q = collections.deque()
q.append([0,0])
board[0][0] = 1
while q:
    x,y = q.popleft()

    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == "1":
            board[nx][ny] = board[x][y]+1
            q.append([nx,ny])
print(board[-1][-1])
