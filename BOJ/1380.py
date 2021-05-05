student=[]
student_print=[]
while True:
    n=int(input())
    if n == 0:
        break
    for _ in range(n):
        student.append(input())
    ans=0
    for _ in range(n*2-1):
        num,alpha = map(str,input().split())
        ans^=int(num)
    student_print.append(student[ans-1])
    student.clear()

for i,v in enumerate(student_print):
    print(i+1,v)