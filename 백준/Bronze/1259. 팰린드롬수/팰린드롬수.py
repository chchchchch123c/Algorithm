def palindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num [len(num) - i - 1]:
            return False
    return True
while True:
    num = input()
    if num == '0':
        break
    if palindrome(num):
        print('yes')
    else:
        print('no')