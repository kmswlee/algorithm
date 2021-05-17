import sys
input = sys.stdin.readline
for _ in range(int(input())):
    password = input().strip()
    left, right = [], []
    for v in password:
        if v == '<':
            if left:
                right.append(left.pop())
        elif v == '>':
            if right:
                left.append(right.pop())
        elif v == '-':
            if left:
                left.pop()
        else:
            left.append(v)
    left.extend(reversed(right))
    print(''.join(left))