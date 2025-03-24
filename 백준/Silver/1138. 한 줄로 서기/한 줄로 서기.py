n = int(input())
p = list(map(int, input().split())) # 순서

arr = [0] * n # 멤버 자리 위치

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == p[i] and arr[j] == 0:
            arr[j] = i+1
            break
        elif arr[j] == 0:
            cnt += 1

print(' '.join(map(str, arr)))