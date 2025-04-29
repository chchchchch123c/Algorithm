# 지폐의 가로 길이에 따른 금액 매핑
money_map = {
    136: 1000,
    142: 5000,
    148: 10000,
    154: 50000
}

# 입력
N = int(input())
total = 0

for _ in range(N):
    width, height = map(int, input().split())
    total += money_map[width]

# 출력
print(total)
