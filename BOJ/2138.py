def flip(head,state,cnt):
    state = head+state
    for i in range(1,n):
        if state[i-1] != result[i-1]:
            cnt+=1
            state[i-1],state[i] = int(not state[i-1]),int(not state[i])
            if i < n-1:
                state[i+1] = int(not state[i+1])
    if state == result:
        return cnt
    else:
        return n+1
n = int(input())
state = list(map(int,input()))
result = list(map(int,input()))
cases1 = flip([int(not state[0]),int(not state[1])],state[2:],1)
cases2 = flip([],state,0)
if cases1+cases2 == (n+1)*2:
    print(-1)
else:
    print(min(cases1,cases2))