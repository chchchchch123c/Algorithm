# 입력 받기
containers = list(map(int, input().split()))

# 총 병 수 계산
total_bottles = sum(containers)

# 보증금(5¢ per bottle) 계산
refund = total_bottles * 5

# 출력
print(refund)
