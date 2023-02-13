from collections import deque

dq = deque() # deque 생성

N = int(input())

for i in range(1, N+1):
    dq.appendleft(i) # 왼쪽에 queue 추가

i = 0
while(len(dq) >1):
    if i % 2 == 0:
        dq.pop()
    else:
        dq.rotate(1) # queue 회전
        
    i+=1

print(dq[0])