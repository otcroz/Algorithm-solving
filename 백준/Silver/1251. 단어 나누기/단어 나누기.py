res = []

word = input()

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        # reverse
        first =first[::-1]
        second = second[::-1]
        third = third[::-1]

        res.append(first + second + third)

print(min(res))