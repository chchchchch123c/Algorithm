num = int(input())
shirt = list(map(int, input().split()))
size = 0
t, p = map(int, input().split())
for i in shirt:
    if i == 0:
        continue
    elif i <= t:
        size += 1
    elif i % t == 0:
        size += i // t
    else:
        size += i // t + 1
bundle = num // p
pen = num % p
print(size)
print(f'{bundle} {pen}')