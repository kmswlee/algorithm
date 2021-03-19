n = int(input())
nums = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())
def back(calc,cur,plus,minus,mul,div):
    global max_calc, min_calc
    if cur == n:
        max_calc = max(max_calc,calc)
        min_calc = min(min_calc,calc)
        return
    if plus > 0:
        back(calc+nums[cur],cur+1,plus-1,minus,mul,div)
    if minus > 0:
        back(calc-nums[cur],cur+1,plus,minus-1,mul,div)
    if mul > 0:
        back(calc*nums[cur],cur+1,plus,minus,mul-1,div)
    if div > 0:
        back(int(calc/nums[cur]),cur+1,plus,minus,mul,div-1)
max_calc = float('-inf')
min_calc = float('inf')
back(nums[0],1,plus,minus,mul,div)
print(max_calc)
print(min_calc)