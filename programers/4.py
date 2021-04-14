def solution(people, limit):
    people.sort(reverse=True)
    res= 0
    left,right = 0,len(people)-1
    while left < right:
        if people[left]+people[right] <= limit:
            left+=1
            right-=1
            res+=1
        else:
            left+=1
            res+=1
        if left == right:
            res+=1
    return res