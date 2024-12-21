def AB(num):
    return (num[0] + num[1]) * (num[0] - num[1])
    
num = list(map(int, input().split()))
print(AB(num))