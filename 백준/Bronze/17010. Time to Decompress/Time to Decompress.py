# Read number of lines
L = int(input())

# Process each line
for _ in range(L):
    n, char = input().split()
    print(char * int(n))
