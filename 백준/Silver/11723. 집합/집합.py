import sys

n = int(sys.stdin.readline())
ss = set()

for _ in range(n):
    stack = sys.stdin.readline().strip().split()
    if len(stack) == 1:
        if stack[0] == "all":
            ss = set([i for i in range(1, 21)])
        else:
            ss = set()
    else:
        func, x = stack[0], stack[1]
        x = int(x)
        if func == "add":
            ss.add(x)
        elif func == "remove":
            ss.discard(x)
        elif func == "check":
            print(1 if x in ss else 0)
        elif func == "toggle":
            if x in ss:
                ss.discard(x)
            else:
                ss.add(x)