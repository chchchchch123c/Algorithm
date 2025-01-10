n = int(input())
test = list(map(int, input().split()))
lst = sorted(test)
total = 0
for i in range(n):
    total += lst[i] / lst[-1] * 100
print(total / n)