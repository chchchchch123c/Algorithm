
n = int(input())
count = 0
yuk = 666
while True:
    if '666' in str(yuk):
        count += 1
        if count == n:
            print(yuk)
            break
    yuk += 1