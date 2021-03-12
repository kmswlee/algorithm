n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = 0
for v1,v2 in zip(sorted(arr1),sorted(arr2,reverse=True)):
    res += v1*v2
print(res)

