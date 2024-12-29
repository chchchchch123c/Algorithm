total = []
for i in range(10):
    num = int(input())
    if num % 42 not in total:
        total.append(num % 42)
print(len(total))