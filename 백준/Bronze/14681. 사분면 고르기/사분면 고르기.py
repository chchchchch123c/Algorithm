a = list(map(int, input().split()))
b = list(map(int, input().split()))

if(a[0] >= 0 and b[0] >= 0):
    print(1)
elif(a[0] <= 0 and b[0] >= 0):
    print(2)
elif(a[0] <= 0 and b[0] <= 0):
    print(3)
else:
    print(4)
    