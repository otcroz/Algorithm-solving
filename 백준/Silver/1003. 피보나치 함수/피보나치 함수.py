T = int(input())

for _ in range(T):
  N = int(input())

  a, b = 1, 0 # 0과 1이 호출된 횟수
  for _ in range(N):
    a, b = b, a+b
  print(a, b)