import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort()
for x, y in sorted(arr):
    print(x, y)