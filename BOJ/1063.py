import sys
input = sys.stdin.readline
king_lo,stone_lo,n = input().split()
king_lo = [ord(king_lo[0])-65,int(king_lo[1])-1]
stone_lo = [ord(stone_lo[0])-65,int(stone_lo[1])-1]
dirs = {
    'R':(1,0), 'L':(-1,0), 'B':(0,-1), 'T':(0,1), 'RT':(1,1), 'LT':(-1,1),'RB':(1,-1), 'LB':(-1,-1)
}
move=[]
for _ in range(int(n)):
    move.append(input().rstrip())

for v in move:
    dx,dy = dirs[v][0],dirs[v][1]
    nx,ny = king_lo[0]+dx,king_lo[1]+dy
    if 0<=nx<8 and 0<=ny<8 :
        if [nx,ny] == stone_lo and 0<=(stone_lo[0]+dx)<8 and 0<=(stone_lo[1]+dy)<8:
            king_lo = [nx,ny]
            stone_lo = [stone_lo[0]+dx,stone_lo[1]+dy]
        elif [nx,ny] != stone_lo:
            king_lo = [nx,ny]

print(chr(65+king_lo[0])+str(king_lo[1]+1))
print(chr(65+stone_lo[0])+str(stone_lo[1]+1))