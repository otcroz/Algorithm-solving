# start, end 지점 사이 방문 지점 저장, 맨해튼 거리 정의
# OEM 순정 내비게이션(짧은 경로, 지점 순서)

N = int(input())
sx, sy, ex, ey = map(int, input().split())

res = [] # 맨해튼 거리 저장
for _ in range(N):
  navi_sum = 0 # 내비 맨해튼 거리 합
  spot = int(input())
  px, py = sx, sy # 시작 지점을 pre 지점으로 초기화
  for _ in range(spot):
    cx, cy = map(int, input().split())
    navi_sum += abs(cx - px) + abs(cy - py)
    px, py = cx, cy # 지점 업데이트
  navi_sum += abs(ex - cx) + abs(ey - cy)
  res.append(navi_sum)

print(res.index(min(res)) + 1)
