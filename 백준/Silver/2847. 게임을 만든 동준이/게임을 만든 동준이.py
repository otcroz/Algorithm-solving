N = int(input())
score = [int(input()) for _ in range(N)]

score.reverse()

sub_cnt = 0
for i in range(N-1):
  while True:
    if score[i] > score[i+1]:
      break
    score[i+1] -= 1
    sub_cnt += 1
print(sub_cnt)