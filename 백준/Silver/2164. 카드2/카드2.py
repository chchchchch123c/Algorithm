import sys
from collections import deque
n = int(sys.stdin.readline())
arr = []
for i in range(1, n + 1):
    arr.append(i)
result = deque(arr)
while len(result) > 1:
    result.popleft()
    result.append(result.popleft())
print(result[0])