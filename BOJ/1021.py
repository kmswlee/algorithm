from collections import deque
n, m = map(int,input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)
nums = list(map(int,input().split()))
res = 0 
for v in nums:
    f_diff = q.index(v)
    b_diff = len(q) - q.index(v)
    if f_diff < b_diff:
        q.rotate(-f_diff)
        q.popleft()
        res+=f_diff
    else:
        q.rotate(b_diff)
        q.popleft()
        res+=b_diff
print(res)