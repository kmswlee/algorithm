s = input()
ch = False
tmp = ''
res = ''
for v in s:
    if v == '<':
        ch = True
        res += tmp[::-1] + '<'
        tmp = ''
    elif v == '>':
        ch = False
        tmp += v
        res += tmp
        tmp = ''
    elif v == ' ' and not ch:
        res += tmp[::-1] + ' '
        tmp =''
    elif v == ' ' and ch:
        tmp+=v
    else:
        tmp+=v
if tmp:
    res+=tmp[::-1]
print(res)

