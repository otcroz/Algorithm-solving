# 인당 1개, 동시 수행 X
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  # 도훈, 상혁의 업무 수행 상태 정의
  DH, SH = -1, -1 

  ta, tb, va, vb = map(int, input().split())

  # A의 업무 수행량 <= B의 업무 수행량
  if tb * vb >= ta * va:
    print(tb * vb)
    continue 
  
  day = 0
  DH_cnt = 0
  SH_cnt = 0

  while True:
    if va == 0 and vb == 0 and DH == -1 and SH == -1:
      break
  
    # 도훈이 일하지 않을 때
    if DH == -1:
      if vb > 0:
        vb -= 1
        DH = 1 # B 업무 수행
        DH_cnt = 0
      elif va > 0:
        va -= 1
        DH = 0 # A 업무 수행
        DH_cnt = 0
    
    # 상혁이 일하지 않을 때
    if SH == -1:
      if va > 0:
        va -= 1
        SH = 0
        SH_cnt = 0
    
    day += 1
    DH_cnt += 1
    
    # 도훈의 업무 수행
    if DH == 1 and DH_cnt == tb:
      DH_cnt = 0
      DH = -1
    elif DH == 0 and DH_cnt == ta:
      DH_cnt = 0
      DH = -1
    
    # 상혁의 업무 수행
    SH_cnt += 1
    if SH == 0 and SH_cnt == ta:
      SH_cnt = 0
      SH -= 1

  print(day)