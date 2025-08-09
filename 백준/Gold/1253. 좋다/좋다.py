import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = 0
arr.sort()
for i in range(n):
    left, right = 0, len(arr) - 1
    while(left < right):
        #print(mid, left, right, arr[left] + arr[right], arr[i])
        if arr[left] + arr[right] == arr[i]:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                res += 1
                #print("arr!",i, arr[i])
                break
        elif arr[left] + arr[right] > arr[i]:
            right -= 1
        else:
            left += 1
print(res)