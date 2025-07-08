N, M = map(int, input().split())
score = list(map(int, input().split()))

for _ in range(M):
  score.sort()
  sum_score = sum(score[:2])
  score[0], score[1] = sum_score, sum_score

print(sum(score))