s = input()
t = input()

def f(t):
    if s == t:
        print(1)
        exit(0)
    if len(t) == 0:
        return
    else:
        if t[-1] == 'A':
            f(t[:-1]) # 마지막 문자 제거
        if t[0] == 'B':
            f(t[1:][::-1]) # 마지막 문자 제거 + 뒤집기

f(t)
print(0)