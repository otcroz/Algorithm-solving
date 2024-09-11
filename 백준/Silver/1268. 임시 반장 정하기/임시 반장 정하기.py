n = int(input())

# 2차원 배열 생성
arr = [list(map(int, input().split()))for _ in range(n)]

person = [[] for _ in range(n)]

for i in range(0, n): # 학생
    for k in range(5): # 학년 
        for j in range(0, n): # 비교군
            if arr[i][k] == arr[j][k] and i != j:
                person[i].append(j)

max_per = 0
max_cnt = 0
for i in range(n):
    person[i] = list(set(person[i]))
    if len(person[i]) > max_cnt:
        max_cnt = len(person[i])
        max_per = i

print(max_per + 1)