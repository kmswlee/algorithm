import sys,collections
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    A,B = map(int,input().split())
    graph[B].append(A)
def bfs(x):
    q = collections.deque()
    q.append(x)
    visited = [0]*(n+1)
    visited[x] = 1
    cnt = 0
    while q:
        num = q.popleft()
        cnt += 1
        for v in graph[num]:
            if not visited[v]:
                q.append(v)
                visited[v] = 1
    return cnt
res = []
max_cnt = 0
for i in range(1,n+1):
    if graph[i]:
        tmp_cnt = bfs(i)
        if max_cnt == tmp_cnt:
            res.append(i)
        elif max_cnt < tmp_cnt:
            res = []
            max_cnt = tmp_cnt
            res.append(i)
print(*res)

# def dfs(x,cnt):
#     if x not in dic:
#         return cnt+1
#     for v in dic[x]:
#         max_cnt = max(cnt,dfs(v,cnt+1))
#     return max_cnt
# res=[]
# max_hacking = 0
# for i in range(1,n+1):
#     if i in dic:
#        max_hacking = max(max_hacking,dfs(i,1))
#     res.append([i,max_hacking])
#     max_hacking = 0
# print(sorted(res,key = lambda x: -x[1]))
