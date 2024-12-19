import sys

input = sys.stdin.readline
output = sys.stdout.write

testCase = int(input().rstrip())

results = []

for _ in range(testCase):
    num = list(map(int, input().rstrip().split()))
    results.append(num[0] + num[1])
    
output("\n".join(map(str, results)) + "\n")