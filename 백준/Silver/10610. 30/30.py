arr = list(map(int, input())) # 문자열 리스트를 숫자로 변환

if sum(arr) % 3 == 0 and (0 in arr) :
    arr.sort(reverse=True)
    result = ''.join(str(s) for s in arr)
    print(result)
    
else: print(-1)