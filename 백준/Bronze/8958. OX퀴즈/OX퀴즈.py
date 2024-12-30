test_case = int(input())
arr = []
for i in range(test_case):
    result = input()
    current_score = 0
    total = 0
    for answer in result:
        if answer == 'O':
            current_score += 1
            total += current_score
        else:
            current_score = 0
    arr.append(total)
for i in arr:
    print(i)