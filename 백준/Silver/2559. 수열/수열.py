import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
pre = [0]
sum_temp = []
mysum = 0

for i in range(0, n):
    mysum += temp[i]
    pre.append(mysum)
    
for i in range(0, n-k+1):
    sum_temp.append(pre[i+k]-pre[i])

print(max(sum_temp))