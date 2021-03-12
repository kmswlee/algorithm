from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[input()]+=1
print(sorted(dic.items(),key = lambda x:(-x[1],x[0]))[0][0])

