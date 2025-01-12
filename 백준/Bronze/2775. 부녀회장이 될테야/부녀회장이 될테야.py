def people(k, n):
    floor = [i for i in range(1, n + 1)]
    for _ in range(k):
        for j in range(1, n):
            floor[j] += floor[j - 1]
    return floor[-1]

num = int(input())
for _ in range(num):
    k = int(input())
    n = int(input())
    print(people(k, n))
