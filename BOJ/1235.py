n = int(input())
arr = [input() for _ in range(n)]
for i in range(1,len(arr[0])+1):
    nums=set()
    for j in range(n):
        nums.add(arr[j][-i:])
    if len(nums) == n:
        print(i)
        break
    

        