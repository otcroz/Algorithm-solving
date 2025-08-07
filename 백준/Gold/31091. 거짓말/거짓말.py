import sys
input = sys.stdin.readline

N = int(input())
L = [0]*(N+1) # n명 이하로 거짓말
U = [0]*(N+1) # n명 이상으로 거짓말

# x명이 거짓말을 하고 있다고 주장
for x in map(int, input().split()):
    if x > 0:
        U[x] += 1
    else:
        L[-x] += 1

# 누적합 계산
LS = [0] * (N+1)
US = [0] * (N+1)

# 거짓말 횟수 누적합 계산
# k: 실제 거짓말한 사람 수
for i in range(1, N+1):
    LS[i] = LS[i-1] + L[i-1] # k명 이상이라고 했지만 실제 x < k로, 잘못된 주장자 수

for i in range(N-1, -1, -1):
    US[i] = US[i+1] + U[i+1] # k명 이하라고 했지만 실제 x > k로, 잘못된 주장자 수

ans = []
for k in range(N+1):
    if LS[k] + US[k] == k: # k명이 거짓말할 때, 거짓말하고 있는 사람 수
        ans.append(k)
print(len(ans))
print(*ans)