n = int(input())
pepole = list(map(int, input().split()))
pepole.sort()
result = 0
time = 0
for i in range(n):
    time += pepole[i]
    result += time
print(result)