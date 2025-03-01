import sys

def stack_sequence(n, sequence):
    stack = []
    result = []
    current = 1
    possible = True

    for num in sequence:
        while current <= num:
            stack.append(current)
            result.append("+")
            current += 1
        
        if stack[-1] == num:
            stack.pop()
            result.append("-")
        else:
            possible = False
            break

    if possible:
        print("\n".join(result))
    else:
        print("NO")

n = int(sys.stdin.readline().strip())
sequence = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack_sequence(n, sequence)