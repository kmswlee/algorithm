import collections
def bfs(n,k):
    q = collections.deque()
    q.append((n,0))
    _set = set()
    while q:
        cur,cnt = q.popleft()
        if cur == k:
            return cnt
        _set.add(cur)
        for v in [cur-1,cur+1,cur*2]:
            if 0 <= v <= 1000000 and v not in _set:
                _set.add(v)
                q.append((v,cnt+1))
n,k = map(int,input().split())
print(bfs(n,k))