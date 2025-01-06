plus_str = input().split("-")

plus_res = []
for item in plus_str:
  tmp = map(int, item.split('+'))
  plus_res.append(sum(tmp))

min_res = plus_res[0]
for i in range(1, len(plus_res)):
  min_res -= plus_res[i]
print(min_res)