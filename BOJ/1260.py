import sys, collections
sys.setrecursionlimit(10000)

n, m, v = map(int,input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if not visited[i] and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    q = collections.deque()
    q.append(v)
    visited[v] = 0
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if visited[i] and matrix[v][i] == 1:
                q.append(i)
                visited[i] = 0
dfs(v)
print()
bfs(v)