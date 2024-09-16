for _ in range(int(input())):
  s = input()
  n = str(int(s) + int(s[::-1])) # s[::-1] 역순으로 출력
  print("YES" if n == n[::-1] else "NO")