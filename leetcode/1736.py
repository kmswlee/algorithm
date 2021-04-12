def sol(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            if i == 0:
                if s[i+1] in '?0123':
                    s[i] = '2'
                else:
                    s[i] = '1'
            elif i == 1:
                if s[0] == '2':
                    s[i] = '3'
                else:
                    s[i] = '9'
            elif i == 3:
                s[i] = '5'
            else:
                s[i] = '9'
    return ''.join(s)
print(sol('??:3?'))