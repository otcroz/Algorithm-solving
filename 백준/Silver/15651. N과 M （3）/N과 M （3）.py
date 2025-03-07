N, M = map(int, input().split())
part = []

def back():
    if len(part) == M:
        print(' '.join(map(str, part)))
        return
    
    for i in range(1, N+1):
        part.append(i)
        back()
        part.pop()

back()