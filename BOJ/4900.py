import sys
input = sys.stdin.readline
seven2ten = {
    '010': '1','093':'2','079':'3','106':'4','103':'5','119':'6','011':'7','127':'8','107':'9','063':'0'
}
ten2seven = {
    '1':'010','2':'093','3':'079','4':'106','5':'103','6':'119','7':'011','8':'127','9':'107','0':'063'
}
while True:
    cases = input().rstrip()
    if cases == 'BYE':
        break
    else:
        cases_tmp = cases[:]
        cases_tmp=cases.replace('=','').split('+')
        a,b = '',''
        for i in range(0,len(cases_tmp[0]),3):
            a+=seven2ten[cases_tmp[0][i:i+3]]
        for j in range(0,len(cases_tmp[1]),3):
            b+=seven2ten[cases_tmp[1][j:j+3]]
        res = ''
        for idx in str(int(a)+int(b)):
            res+=ten2seven[idx]
        print(cases+res)