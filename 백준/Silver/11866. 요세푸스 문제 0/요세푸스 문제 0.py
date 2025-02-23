pepole = []
index = 0
result = []
n, k = map(int, input().split())
for i in range(1, n + 1):
    pepole.append(i)
while pepole:
    index = (index + k - 1) % len(pepole)
    result.append(pepole.pop(index))
print('<' + ', '.join(map(str, result)) + '>')