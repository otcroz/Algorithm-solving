num = int(input())

arr = [i+1 for i in range(num)]

cnt = 0
while(len(arr)> 0):
    item = arr.pop(0)
    if cnt % 2 == 1:
        arr.append(item)
    else:
        print(item, end=' ')
    cnt+=1