arr=['aba','abab','abcabc','a']
check=set()
ans,flag=0,True

for word in arr:
    for j in range(len(word)):
        if j == 0:
            check.add(word[j])
        elif word[j-1] != word[j] and word[j] in check:
            flag=False
            break
        elif word[j-1] != word[j] and word[j] not in check:
            check.add(word[j-1])
    if flag:
        ans+=1
    check.clear()
    flag=True
print(ans)
