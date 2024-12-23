def ABC(a, b, c):
    return a + b - c
def ABC2(a, b, c):
    return int((str(a) + str(b))) - c   
one = int(input())
two = int(input())
thr = int(input())
print(ABC(one, two, thr))
print(ABC2(one, two, thr))