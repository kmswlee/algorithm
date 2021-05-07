def sol(s,d):
    dic={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    ans=[]
    for i in range(s,d+1):
        ans.append([dic[i//10]+dic[i%10] if i//10 != 0 else dic[i%10],i])
    ans.sort()
    for i in range(0,len(ans)):
        if i%10 == 0 and i != 0:
            print()
        print(ans[i][1],end=' ')
s,d=input().split()
sol(int(s),int(d))