import sys
from collections import Counter
result = []
n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))
counter = Counter(list1)
for i in list2:
    result.append(counter[i])
print(*result)