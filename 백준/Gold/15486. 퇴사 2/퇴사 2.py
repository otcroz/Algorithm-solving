import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
d = [0] * (N+1)

for i in range(1, N+1):
    a, b = map(int, input().split())
    d[i]= max(d[i-1], d[i])
    fin = i+a-1 # 상담이 끝나는 날
    if fin <= N: # 상담이 끝나는 날 <= 최대 상담일
        d[fin] = max(d[i-1] + b, d[fin])

print(max(d))