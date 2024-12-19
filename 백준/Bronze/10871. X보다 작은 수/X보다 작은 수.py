N, X = map(int, input().split())
a = list(map(int, input().split()))
print(" ".join(str(num) for num in a if num < X))