time_per = []
per = 0

N = int(input())
time = list(map(int, input().split()))

time.sort()

for i in range(0, N):
    per += time[i]
    time_per.append(per)
    

print(sum(time_per))
