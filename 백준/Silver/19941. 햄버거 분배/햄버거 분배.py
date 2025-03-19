N, K = map(int, input().split())
table = list(input())
cnt = 0

for idx in range(N):
    if table[idx] == 'P':
        for i in range(max(idx-K, 0), min(idx+K+1, N)):      
            if table[i] == 'H':
                table[i] = 'X'
                cnt += 1
                break

print(cnt)