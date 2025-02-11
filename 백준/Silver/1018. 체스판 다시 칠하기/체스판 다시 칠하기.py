import sys
board = []
result = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    board.append(sys.stdin.readline().strip())
for i in range(n - 7):
    for j in range(m - 7):
        count1, count2 = 0, 0
        for x in range(8):
            for y in range(8):
                current_color = board[i + x][j + y]
                if (x + y) % 2 == 0:
                    if current_color != 'W':
                        count1 += 1
                    if current_color != 'B':
                        count2 += 1
                else:
                    if current_color != 'B':
                        count1 += 1
                    if current_color != 'W':
                        count2 += 1
        result.append(count1)
        result.append(count2)
print(min(result))