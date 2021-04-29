def sol(n,k):
    idx=0
    arr=[i for i in range(1,n+1)]
    ans=[]
    while arr:
        idx=(idx+(k-1))%len(arr)
        num=arr.pop(idx)
        ans.append(str(num))
    
    print("<%s>"%(", ".join(ans)))

sol(7,3)