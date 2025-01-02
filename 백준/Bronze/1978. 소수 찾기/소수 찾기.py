def de(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
num = int(input())
lst = list(map(int, input().split()))
decimal = 0
for i in lst:
    if de(i):
        decimal += 1
print(decimal)