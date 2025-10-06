# 최소 1개 모음, 최소 2개 자음
# 알파벳이 증가하는 순서 배열
# abc 0 bac x
# 문자의 종류는 C가지. > C개의 문자, 가능성 있는 암호들을 구하는 프로그램

L, C = map(int, input().split())
arr = list(input().split())
arr.sort() # 정렬

vowels = ['a','e','i','o','u']
v = [0] * C

def back(j, cnt, strs):
  if cnt == L:
    # 자음, 모음 개수 파악하기
    v_count = 0
    not_v_count = 0
    for s in strs:
      if s in vowels:
        v_count += 1
      else:
        not_v_count += 1
    if v_count >= 1 and not_v_count >= 2:
      print(''.join(map(str, strs)))
  else:
    for i in range(j, len(arr)):
      if not v[i]:
        v[i] = 1
        strs.append(arr[i])
        back(i+1, cnt+1, strs)
        strs.pop()
        v[i] = 0

back(0,0, [])