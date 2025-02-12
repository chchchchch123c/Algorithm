import sys
n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().strip().split()))
for i in b:
    print(1 if i in a else 0)