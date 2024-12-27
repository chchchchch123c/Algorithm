A = int(input())
B = int(input())
C = int(input())

def AXBXC(A, B, C):
    return A * B * C

value = AXBXC(A, B, C)

for i in range(10):
    print(str(value).count(f'{i}'))