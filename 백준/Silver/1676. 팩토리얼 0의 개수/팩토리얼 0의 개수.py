import math
n = int(input())
fac = math.factorial(n)
total = 0
for i in str(fac)[::-1]:
    if i == '0':
        total += 1
    else:
        break
print(total)