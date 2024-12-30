s = input()
arr = []
for i in range(26):
    alpha = chr(97 + i)
    arr.append(s.find(alpha))
print(*arr)