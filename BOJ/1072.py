import sys
X,Y=map(int,sys.stdin.readline().split())
check_Z=(100*Y)//X
if check_Z >= 99:
    print(-1)
else:
    start=0
    end=1000000000
    while start <= end:
        mid = (start+end)//2
        if ((Y+mid)/(X+mid))*100 > check_Z:
            end = mid-1
        else:
            start = mid+1
    print(end+1)
        