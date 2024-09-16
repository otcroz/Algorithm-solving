s = input()
arr = [0 for _ in range(26)]

for i in range(len(s)):
  arr[ord(s[i]) - 97] += 1

[print(arr[i], end =' ') for i in range(26)]