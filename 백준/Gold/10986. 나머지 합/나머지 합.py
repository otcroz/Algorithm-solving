import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

prefix = 0
mod_count = [0]*m # prefix 나머지가 몇 번 나왔는지 저장
mod_count[0] = 1 # mod가 0일 때 당연하게도 나눠떨어짐

result = 0
for num in a: # 집합을 만드는 횟수
    prefix = (prefix + num) % m # 누적합의 나머지
    # 같은 나머지를 가지는 누적합 => 그 사이 구간은 m으로 나누어짐
    result += mod_count[prefix] # 같은 나머지를 갖는 누적합으로 (i, j)쌍을 만들 수 있음.
    mod_count[prefix] += 1 # 나머지 경우의 수 추가
print(result)