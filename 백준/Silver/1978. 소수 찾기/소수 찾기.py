cnt = 0

N = int(input())

arr = list(map(int, input().split()))

def func(i):
    global cnt
    if i == 1:
        return False
    for j in range(2, int(i**0.5)+ 1):
        if i % j == 0:
            return False
    return True

for i in arr:
    if func(i):
        cnt += 1

print(cnt)