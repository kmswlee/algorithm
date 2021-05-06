num=input()
cnt=0
while len(num) > 1:
    num=str(sum(list(map(int,num))))
    cnt+=1
print(cnt)
print(['YES','NO'][int(num)%3])