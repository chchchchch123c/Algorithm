le = int(input())
string = input()
total = 0
for i in range(le):
    value = ord(string[i]) - 97 + 1
    total += value * (31 ** i)
print(total % 1234567891)