import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort(key=lambda p: (p[1], p[0]))
for x, y in arr:
    print(x, y)