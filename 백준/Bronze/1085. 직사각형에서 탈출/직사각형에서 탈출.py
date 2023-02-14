x, y, w, h = map(int, input().split())

min = w - x

if x-0 < min:
    min = x - 0

if h - y < min:
    min = h - y

if y - 0 < min:
    min = y - 0

print(min)