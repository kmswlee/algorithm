from sys import stdin
total,kim,imm=map(int,stdin.readline().split())
res=0
while kim != imm:
    kim=(kim+1)//2
    imm=(imm+1)//2
    res+=1
print(res)