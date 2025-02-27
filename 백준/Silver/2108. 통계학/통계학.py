import sys
freq = {}
arr = []
n = int(sys.stdin.readline())
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
sum_arr = round(sum(arr) / len(arr))
middle_arr = arr[len(arr) // 2]
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
max_count = max(freq.values())
modes = sorted([num for num, count in freq.items() if count == max_count])
mode = modes[1] if len(modes) > 1 else modes[0]
range_arr = arr[-1] - arr[0]
print(sum_arr)
print(middle_arr)
print(mode)
print(range_arr)