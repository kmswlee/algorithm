import sys, collections
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = collections.defaultdict(list)
f_list = [False]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = collections.deque()
q.append((1,0))
f_list[1] = True
res = 0
while q:
    num,cnt = q.popleft()
    for v in graph[num]:
        if f_list[v]:
            continue
        if not f_list[v] and cnt < 2:
            q.append((v,cnt+1))
            f_list[v] = True
            res+=1
        elif cnt == 2:
            break
print(res)