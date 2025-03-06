N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
part = []

def back(start):
    global cnt
    if len(part) >= 1 and sum(part) == S:
        cnt += 1
    for i in range(start, N):
        part.append(arr[i])
        back(i+1)
        part.pop()

back(0)
print(cnt)