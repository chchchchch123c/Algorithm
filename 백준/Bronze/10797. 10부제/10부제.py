day = int(input())  # 날짜의 일의 자리 숫자 입력
cars = list(map(int, input().split()))  # 5대의 자동차 번호 입력

count = 0
for car in cars:
    if car == day:
        count += 1

print(count)
