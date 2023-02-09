answer = []

size = int(input())
a = list(map(int, input().split())) # sort_list

b = a.copy() # origin_list
a.sort()

for i in range(size):
        index = a.index(b[i])
        
        answer.append(index)
        a[index] = None
        
for i in answer:
    print(i, end=" ")