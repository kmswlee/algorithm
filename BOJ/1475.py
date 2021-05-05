import collections
num=input()
num=num.replace('9','6')
num=list(map(int,num))
num=collections.Counter(num)
num[6]=(num[6]+1)//2
print(max(num.values()))