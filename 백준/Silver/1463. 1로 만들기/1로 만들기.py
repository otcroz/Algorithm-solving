x = int(input())

d = [0] * 1000001

for i in range(2, x+1):
    d[i] = d[i-1] + 1 # 1을 빼줌
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1) # 3을 나눠줬으니 1을 다시 더해줌
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1) # 2를 나눠줬으니 1을 다시 더해줌

print(d[x])