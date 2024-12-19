N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    a.append(list(map(int, input().split())))
for i in range(N):
    b.append(list(map(int, input().split())))
result = []
for a_row, b_row in zip(a, b):
    result.append([x + y for x, y in zip(a_row, b_row)])
for row in result:
    print(*row)
