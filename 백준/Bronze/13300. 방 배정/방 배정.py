n, k = map(int, input().split())
arr = [[0, 0] for _ in range(7)]

for _ in range(n):
    sex, grade = map(int, input().split())
    arr[grade][sex] += 1

cnt = 0
for i in range(7): # 학년
    for j in range(2): # 성별
        if arr[i][j] > 0:
            cnt+=1
            if arr[i][j] > k:
                cnt += 1
print(cnt)