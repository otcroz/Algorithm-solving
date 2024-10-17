N = int(input())

sum = 1
count = 1
while True:
    if N == 1:
        print(count)
        break
    if N <= sum:
        print(count)
        break
    sum += 6 * count
    count += 1