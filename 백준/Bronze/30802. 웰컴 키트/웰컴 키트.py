import sys
input = sys.stdin.readline
N = int(input())
res = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠
cnt = 0
for size in res:
    if size == 0:
        continue
    elif size < T:
        cnt += 1
    elif size % T == 0:
        cnt += size // T
    else:
        cnt += size // T + 1

# 펜
pen_Q = N // P
pen_R = N % P

print(cnt)
print(pen_Q, pen_R)