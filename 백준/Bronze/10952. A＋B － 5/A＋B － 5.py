while True:
    num = list(map(int, input().split()))
    if num[0] == 0 and num[1] == 0: break
    print(num[0] + num[1])