n = int(input())
s = input()

cnt = []

red_right = s.rstrip('R')
cnt.append(red_right.count('R'))

blue_right = s.rstrip('B')
cnt.append(blue_right.count('B'))

red_left = s.lstrip('R')
cnt.append(red_left.count('R'))

blue_left = s.lstrip('B')
cnt.append(blue_left.count('B'))

print(min(cnt))