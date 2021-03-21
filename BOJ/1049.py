from sys import stdin
m,n=map(int,stdin.readline().split())
min_six_price,min_one_price=float('inf'),float('inf')
for i in range(n):
    six_price,one_price=map(int,stdin.readline().split())
    if min_six_price > six_price:
        min_six_price=six_price
    if min_one_price > one_price:
        min_one_price=one_price
if min_one_price*6 < min_six_price:
    ans=min_one_price*m
else:
    six_pakage_num,one_pakage_num=divmod(m,6)
    if min_six_price < one_pakage_num*min_one_price:
        ans=(six_pakage_num+1)*min_six_price
    else:
        ans=six_pakage_num*min_six_price + one_pakage_num*min_one_price
print(ans)