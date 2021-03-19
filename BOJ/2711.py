n = int(input())
while n:
    location , s = input().split()
    location = int(location) - 1
    s = list(s)
    s[location] = ''
    print(''.join(s))
    n-=1

