s = input()
n = s.count('a')

s += s[0:n-1] # 슬라이싱 윈도우 길이만큼 추가
min_val = 1000
for i in range(len(s)-(n-1)):
  min_val = min(min_val, s[i:i+n].count('b'))

print(min_val)