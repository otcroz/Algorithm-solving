N, M = map(int, input().split())
part = []

def back(start):
    if len(part) == M:
        print(" ".join(map(str, part)))
    for i in range(start, N + 1):
        part.append(i)
        back(i+1)
        part.pop()

back(1)