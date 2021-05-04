n=int(input())
cand=[]
for _ in range(n):
    cand.append(int(input()))
dasom,cand,cnt=cand[0],cand[1:],0
while cand[-1]>dasom:
    dasom+=1
    cand[-1]-=1
    cnt+=1
    cand.sort()
print(cnt)