def binary_search(num):
    start, end = 0, len(arr1) - 1
    while(start <= end):
        mid = (start + end) // 2

        if (arr1[mid] > num):
            end = mid - 1
        elif (arr1[mid] < num):
            start = mid + 1
        else:
            return 1
            
    return 0
    
case = int(input())

i = 0
while(i < case):

    N = int(input())
    arr1 = list(map(int, input().split()))
    arr1.sort()

    M = int(input())
    arr2 = list(map(int, input().split()))
    
    for n in arr2:
        print(binary_search(n))
    i+=1