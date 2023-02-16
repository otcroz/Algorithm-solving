self_nums = []

i = 1
while i <= 10000:

    num = str(i)

    sum_nums = 0
    for k in range(0, len(num)):
        sum_nums += int(num[k])

    num = int(num) + sum_nums
    self_nums.append(num)
    
    if i not in self_nums:
        print(i)

    i+=1