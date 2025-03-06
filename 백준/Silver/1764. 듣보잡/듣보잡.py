import sys
n, m = map(int, sys.stdin.readline().split())
result = []
never_hear_see = set()
never_see = set()
for _ in range(n):
    never_hear_see.add(sys.stdin.readline().rstrip())
for _ in range(m):
    never_see.add(sys.stdin.readline().rstrip())
for i in never_hear_see:
    if i in never_see:
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)