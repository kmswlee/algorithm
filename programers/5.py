def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    res = 0
    for v in routes:
        if v[0] <= camera < v[1]:
            continue
        elif camera < v[0]:
            res+=1
            camera = v[1]
    return res