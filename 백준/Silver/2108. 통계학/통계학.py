N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

arr.sort()

avg = round(sum(arr) / N)
median = arr[N//2]
ran = max(arr) - min(arr)
mode = 0

list(set(arr))

# 최빈값
dic = dict()

for i in arr:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

mx = max(dic.values())
mx_arr = []

for i in dic:
  if mx == dic[i]:
    mx_arr.append(i)

if len(mx_arr) > 1:
  mode = mx_arr[1]
else:
  mode = mx_arr[0]

print(avg)
print(median)
print(mode)
print(ran)