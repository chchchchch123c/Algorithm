n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
money.sort(reverse=True)
count = 0
for i in money:
    if i <= k:
        count += k // i
        k %= i
print(count)