import sys
num, B = input().split()
B = int(B)
res = 0
for i,v in enumerate(num[::-1]):
    if v.isdigit():
        tmp = int(v)
    else:
        tmp = ord(v) - 55
    res += tmp * (B**i)
sys.stdout.write(str(res))