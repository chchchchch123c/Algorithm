test_case = int(input())
for _ in range(test_case):
    r, s = input().split()
    for i in s:
        print(i * int(r), end="")
    print()