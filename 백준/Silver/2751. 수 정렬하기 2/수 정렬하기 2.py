import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
lst = sorted(arr)
for i in lst:
    print(i)