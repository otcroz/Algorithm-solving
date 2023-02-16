doc = input()
word = input()

cnt = 0
while word in doc:
    cnt += 1
    doc = doc[doc.index(word) + len(word):]

print(cnt)