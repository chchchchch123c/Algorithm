def F(x: str) -> str:
    first_digit = int(x[0])
    length = len(x)
    return str(first_digit * length)

def is_FA(x: str) -> str:
    seen = set()
    while x not in seen:
        seen.add(x)
        x = F(x)
    return "FA"

# 입력 받기
x = input().strip()
print(is_FA(x))
