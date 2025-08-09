T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

prefix_a = []
prefix_b = []

for i in range(n):
    mysum = 0
    for j in range(i, n):
        mysum += a[j]
        prefix_a.append(mysum)
mysum = 0
for i in range(m):
    mysum = 0
    for j in range(i, m):
        mysum += b[j] 
        prefix_b.append(mysum)

prefix_a.sort()
prefix_b.sort()

res = 0

def biselection_left(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def biselection_right(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right

for sum_a in prefix_a:
    temp = T - sum_a # sum_a + sum_b = T이므로, B에서 필요한 부분합.
    left = biselection_left(prefix_b, temp) # target 이상이 처음 나왔을 때 left
    right = biselection_right(prefix_b, temp) # target 이하가 처음 나왔을 때 right
    res += right - left + 1 # 인덱스이므로 1을 더해줌.

print(res)