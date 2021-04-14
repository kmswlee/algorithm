def solution(number, k):
    res = ""
    for v in number:
        if res and res[-1] < v:
            while k > 0 and res and res[-1] < v:
                res=res[:-1]
                k-=1
            res+=v
        else:
            res+=v
    return res if not k else res[:-k]

print(solution("44444",3))
