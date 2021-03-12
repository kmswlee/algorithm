import collections
name = input()
dic = collections.Counter(name)
cnt = 0
for v in dic.values():
    if v%2:
        cnt+=1
    if cnt >= 2:
        print("I'm Sorry Hansoo")
        break
if cnt <= 1:
    res = ""
    for s,v in dic.items():
        if v % 2:
            res+=s
            dic[s]-=1
            break
    for s,v in sorted(dic.items(),key=lambda x:x[0],reverse=True):
        for i in range(v):
            if i % 2:
                res = s+res
            else:
                res+=s
    print(res)