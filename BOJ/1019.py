from sys import stdin

N=int(stdin.readline().rstrip())
ans=[0]*10
start,digit=1,1
def cal(x,digit):
    while x > 0:
        ans[x%10]+=digit
        x//=10
while start <= N:
    while N % 10 != 9 and start <= N:
        cal(N,digit)
        N-=1
    if N < start:
        break
    while start % 10 != 0 and start <= N:
        cal(start,digit)
        start+=1
    start//=10
    N//=10
    for i in range(10):
        ans[i]+=(N-start+1)*digit
    digit*=10

print(' '.join(map(str,ans)))