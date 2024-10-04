T = int(input())


for _ in range(T):
    res = []
    s = list(map(str, input()))

    for i in s:
        if i == '(':
            res.append('(')
        elif len(res) != 0 and res[-1] == '(' and i == ')':
            res.pop()
        else:
            res.append(')')
    if len(res) == 0:
        print('YES')
    else:
        print('NO')