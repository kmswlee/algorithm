import collections, sys,itertools
input = sys.stdin.readline

col,row,high = map(int,input().split())
grid = [[] for _ in range(high)]
for i in range(high):
    for j in range(row):
        grid[i].append(list(map(int,input().split())))
if 0 not in list(itertools.chain.from_iterable(list(itertools.chain.from_iterable(grid)))):
    print(0)
else:
    q = collections.deque()
    def bfs():
        while q :
            x,y,z = q.popleft()
            for dx,dy,dz in [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1]]:
                nx,ny,nz = x + dx, y + dy, z + dz
                if 0 <= nx < row and 0 <= ny < col and 0 <= nz < high and grid[nz][nx][ny] == 0:
                    q.append((nx,ny,nz))
                    grid[nz][nx][ny] = grid[z][x][y] + 1

    for z in range(high):
        for x in range(row):
            for y in range(col):
                if grid[z][x][y] == 1:
                    q.append((x,y,z))
    bfs()
    grid = list(itertools.chain.from_iterable(list(itertools.chain.from_iterable(grid))))
    if 0 in grid:
        print(-1)
    else:
        print(max(grid)-1)