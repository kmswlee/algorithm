import sys
input = sys.stdin.readline
visited = [[0]*6 for _ in range(6)]
ch = False
zeros = False
cur = input().rstrip()
start = cur
visited[ord(cur[0])-65][int(cur[1])-1] = 1
def checked(cur,nxt):
    cur = [ord(cur[0])-65,int(cur[1])-1]
    nxt = [ord(nxt[0])-65,int(nxt[1])-1]
    move_list = []
    for dx,dy in [[-2,-1],[-2,1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2]]:
        nx,ny = cur[0]+dx,cur[1]+dy
        if 0 <= nx < 6 and 0 <= ny < 6 and not visited[nx][ny]:
            move_list.append([nx,ny])
    return True if nxt in move_list else False

for _ in range(35):
    next_move = input().rstrip()
    if checked(cur,next_move):
        cur = next_move
        visited[ord(cur[0])-65][int(cur[1])-1] = 1
    else:
        ch = True
        cur = next_move

if 0 in sum(visited,[]):
    zeros = True
visited[ord(start[0])-65][int(start[1])-1] = 0
if ch or zeros or not checked(cur,start) :
    print('Invalid')
else:
    print('Valid')