N, M = map(int, input().split())
majority = M // 2 + 1

count = 0
for _ in range(N):
    votes = input()
    if votes.count('O') >= majority:
        count += 1

print(count)
