import sys

input = lambda : sys.stdin.readline().rstrip()

N, X = map(int, input().split())
day = list(map(int, input().split()))

if max(day) == 0:
    print('SAD')
    exit(0)

value = sum(day[:X])
max_value = value
cnt = 1

# 슬라이딩 윈도우
for i in range(X, N):
    value += day[i]
    value -= day[i-X]
    
    if value > max_value:
        max_value = value
        cnt = 1
    elif value == max_value:
        cnt += 1

else:
    print(max_value)
    print(cnt)