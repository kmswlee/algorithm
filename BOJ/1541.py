exp = input().split('-')
res = [sum(list(map(int,v.split('+')))) for v in exp]
print(res[0]-sum(res[1:]))

