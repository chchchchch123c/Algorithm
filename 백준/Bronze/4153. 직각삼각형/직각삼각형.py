while True:
    num = list(map(int, input().split()))
    if num[0] ==0 and num[1] == 0 and num[2] == 0:
        break
    py = sorted(num)
    if (py[0] ** 2 + py[1] ** 2) == py[2] **2:
        print('right')
    else:
        print('wrong')