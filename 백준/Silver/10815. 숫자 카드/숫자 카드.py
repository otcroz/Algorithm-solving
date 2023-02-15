res =[]

def binary_sort(left, right, num):
    while(left <= right):
        mid = (left + right) // 2
        
        if num > arr1[mid]:
            left = mid + 1
            
        elif num < arr1[mid]:
            right = mid - 1
            
        elif num == arr1[mid]:
            return True
        
    return False
    
N = int(input())
arr1 = list(map(int, input().split())) # 소유 숫자 카드
arr1.sort()

M = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if binary_sort(0, len(arr1) -1, i):
        res.append('1')
    else:
        res.append('0')


print(' '.join(res))
