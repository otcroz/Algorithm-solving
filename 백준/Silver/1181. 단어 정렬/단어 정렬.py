word = []
N = int(input())

for i in range(N):
    word.append(input())

word = set(word) # 중복 제거
word = list(word) # 리스트 변환

word.sort() # 알파벳순
word.sort(key=len) # 길이순

for i in range(len(word)):
    print(word[i])
