n = int(input())
text = list(input())

for _ in range(n - 1):
    word = input()
    for i in range(len(word)):
        if text[i] == word[i]:
            continue
        else:
            text[i] = '?'
print(*text, sep="")