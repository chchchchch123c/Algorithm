# Read the first line: m = number of clauses, n = number of variables
m, n = map(int, input().split())

# Read and discard the next m lines (the actual clauses)
for _ in range(m):
    input()

# Output Øyvind's judgement
if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")
