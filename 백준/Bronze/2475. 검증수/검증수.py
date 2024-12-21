def number(nums):
    listNum = []
    for num in nums:
        listNum.append(num ** 2)
    total = 0
    for value in listNum:
        total += value
    return total % 10
num = list(map(int, input().split()))
print(number(num))