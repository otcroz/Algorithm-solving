N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
#print(money)
left = max(money) # M <= N 이므로, 적어도 각 돈의 최댓값은 되어야 한다.
right = sum(money) # 돈의 합이 최대. 한 번에 빌리는 경우

res = 0
while(left <= right):
    mid = (left + right) // 2

    total = 0 # 총합
    cnt = 0 # 실제 인출 횟수
    for x in money:
        if total+x <= mid: # 인출 금액보다 적거나 같을 때(모자란 경우에만 인출)
            total += x
        else:
            cnt += 1
            total = 0
            total += x
    if total: # 값이 남은 경우
        cnt += 1
    if cnt > M: # 횟수가 많은 경우
        left= mid+1
    else: # 횟수가 적거나 같은 경우(일단 res에는 저장)
        right=mid-1
        res = mid
print(res)