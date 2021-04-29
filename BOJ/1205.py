n,new_score,p = map(int,input().split())


if n:
    ranking_board = list(map(int,input().split()))
    ranking_board.append(new_score)
    ranking_board.sort(reverse=True)
    idx = ranking_board.index(new_score)+1
    if idx > p:
        print(-1)
    else:
        if n == p and ranking_board[-1] == new_score:
            print(-1)
        else:
            print(idx)
else:
    print(1)

